import cv2
import pytesseract
import numpy as np

'''
[[903. 199.]
[179. 200.]
[159. 593.]
[938. 581.]]

----lexsort로 인한 인덱스 변화----

[[159. 593.]
[179. 200.]
[903. 199.]
[938. 581.]]

---- if문으로 순서 바꾼 후----

[[179. 200.]
[159. 593.]
[938. 581.]
[903. 199.]]
'''

def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    pts = pts[idx]
    print(pts)
    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]
    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]
    print(pts)
    return pts

img = cv2.imread('./AI/images/businesscard2.jpg')
dw, dh = 700, 400
srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)

dst = np.zeros((dh, dw), np.uint8)
src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cpy = img.copy()
for pts in contours:
    if cv2.contourArea(pts) < 500:
        continue
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2)
    # print(approx)
    print(approx.reshape(4, 2).astype(np.float32))
    
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(img, pers, (dw, dh))
    dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(dst_gray, lang='kor+eng'))
    
    cv2.imshow('img', img)
    cv2.imshow('cpy', cpy)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    
'''
ST. MARY'S 개개 ORTHOPEDICS

YY 성모튼튼 정형외과

송 금 비 도수치료사 /실장

서울 관악구 남현동 1057-22 HAYS 3S

(남부순환로 2056 남서울농협 3층)

Tel. 02.583.5544 Fax. 02.583.8181

도수치료실 070.4415.6114 Mobile. 010.4532.1687
'''