# CORD 주석(JSON)에서 단어 텍스트와 박스를 추출한 뒤,
# 같은 y대역의 단어들을 한 줄로 묶어 라인 이미지(.png)와 정답(.gt.txt)을 만드는 스크립트라 한다.
# 생성된 라인 쌍은 Tesseract 훈련(.lstmf 생성) 단계의 입력으로 사용한다 한다.

import json, math
from pathlib import Path
from PIL import Image
import numpy as np
from sklearn.cluster import DBSCAN          

RAW = Path("data/cord_raw")                 # 앞 단계에서 저장한 원본 PNG/JSON 위치라 한다
GT  = Path("data/gt_lines")                 # 라인 단위 GT를 저장할 위치라 한다
GT.mkdir(parents=True, exist_ok=True)

def extract_words_boxes(meta):
    """
    CORD JSON에서 (text, bbox[x1,y1,x2,y2]) 리스트를 뽑아내는 함수라 한다.
    데이터셋 버전에 따라 키가 다를 수 있어 필요하면 이 부분을 맞춰준다 한다.
    """
    words = []
    if isinstance(meta, dict):
        # 흔히 'ocr' 또는 'annotations' 같은 루트 아래에 'words' 리스트가 존재한다 한다
        ocr = meta.get('ocr') or meta.get('annotations') or meta.get('valid_line')
        if isinstance(ocr, dict) and 'words' in ocr:
            for w in ocr['words']:
                t = w.get('text') or w.get('transcription')         # 단어 텍스트 필드 후보라 한다
                b = w.get('box') or w.get('bbox') or w.get('polygon')# 박스 좌표 필드 후보라 한다
                if t and b:
                    # polygon(다각형)인 경우 외접 사각형으로 변환한다 한다
                    if len(b) > 4:
                        xs = b[0::2]; ys = b[1::2]
                        b = [min(xs), min(ys), max(xs), max(ys)]
                    words.append((t, b))
        elif isinstance(ocr, list):
            # 루트가 리스트인 변형 스키마도 대비한다 한다
            for w in ocr:
                t = w.get('text') or w.get('transcription')
                b = w.get('box') or w.get('bbox') or w.get('polygon')
                if t and b:
                    if len(b) > 4:
                        xs = b[0::2]; ys = b[1::2]
                        b = [min(xs), min(ys), max(xs), max(ys)]
                    words.append((t, b))
    return words

def group_into_lines(words):
    """
    단어들의 y중심값을 기준으로 DBSCAN으로 같은 줄을 묶는 함수라 한다.
    eps 값은 이미지 해상도에 따라 조정한다. 15~25 픽셀 대역에서 탐색해도 된다 한다.
    """
    if not words: return []
    ys = np.array([ (b[1]+b[3])/2 for _, b in words ]).reshape(-1,1)  # 각 단어의 y중심을 계산한다 한다
    clustering = DBSCAN(eps=18, min_samples=1).fit(ys)                # 같은 y대역을 같은 라벨로 묶는다 한다
    groups = {}
    for (text, box), label in zip(words, clustering.labels_):
        groups.setdefault(label, []).append((text, box))

    lines = []
    for g in groups.values():
        # 같은 줄 내에서 x좌표(왼→오)로 정렬하여 문장을 구성한다 한다
        g = sorted(g, key=lambda x: x[1][0])
        text_line = " ".join([t for t,_ in g]).strip()
        xs = [b[0] for _,b in g]; ys_ = [b[1] for _,b in g]; xe = [b[2] for _,b in g]; ye = [b[3] for _,b in g]
        box = [min(xs), min(ys_), max(xe), max(ye)]                  # 줄 외접 박스를 만든다 한다
        lines.append((box, text_line))

    # 줄 상단 y로 정렬하여 문서 순서를 맞춘다 한다
    lines.sort(key=lambda x: x[0][1])
    return lines

def run():
    for j in sorted(RAW.glob("*.json")):                              # 각 JSON 주석 파일에 대해 순회한다 한다
        with open(j, "r", encoding="utf-8") as f:
            meta = json.load(f)
        png = RAW / (j.stem + ".png")                                 # 동일 stem의 PNG를 찾는다 한다
        if not png.exists():
            continue

        words = extract_words_boxes(meta)                              # (텍스트, 박스) 목록을 추출한다 한다
        if not words:
            print("no words:", j.name)
            continue

        lines = group_into_lines(words)                                # 줄 단위로 묶는다 한다
        if not lines:
            continue

        img = Image.open(png).convert("RGB")
        for i, (box, text) in enumerate(lines):
            x1,y1,x2,y2 = [int(v) for v in box]
            # 크롭 안정성을 위해 약간의 여유를 둔다 한다
            x1 = max(0, x1-3); y1 = max(0, y1-2)
            x2 = min(img.width,  x2+3); y2 = min(img.height, y2+2)
            crop = img.crop((x1,y1,x2,y2))

            out_img = GT / f"{j.stem}_{i:02d}.png"                    # 라인 이미지 파일명이라 한다
            out_txt = GT / f"{j.stem}_{i:02d}.gt.txt"                 # 라인 정답 텍스트 파일명이라 한다
            crop.save(out_img)
            out_txt.write_text(text + "\n", encoding="utf-8")

    print("Done. line GT saved to:", GT)

if __name__ == "__main__":
    run()
