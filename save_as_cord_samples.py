# 연습 데이터 : https://huggingface.co/datasets/naver-clova-ix/cord-v2
# CORD-v2 데이터셋 다운받고 이미지(png)와 주석(json)을 로컬에 저
import json
from datasets import load_dataset
from pathlib import Path
from PIL import Image

out = Path("data/cord_raw")
out.mkdir(parents=True, exist_ok=True)

ds = load_dataset("naver-clova-ix/cord-v2", split="train")
print("Columns:", ds.column_names)
print("Total:", len(ds))

# 샘플 하나 꺼내
item = ds[0]
# 버전에 따라 ground_truth / gt_parse 키 사
meta = item.get("ground_truth") or item.get("gt_parse")
print("Meta type:", type(meta))
print("Meta preview:", (meta if isinstance(meta, str) else str(meta))[:600])

# 샘플 50개만 저
N = 50
for i in range(min(N, len(ds))):
    img: Image.Image = ds[i]["image"]
    meta = ds[i].get("ground_truth") or ds[i].get("gt_parse")
    (out / f"{i:03d}.png").parent.mkdir(parents=True, exist_ok=True)
    img.save(out / f"{i:03d}.png")
    
    # 메타가 문자열이면 JSON으로 파싱 / 딕셔너리면 그대로 저장
    if isinstance(meta, str):
        try:
            meta = json.loads(meta)
        except Exception:
            pass
    with open(out / f"{i:03d}.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

print("Saved to:", out)
