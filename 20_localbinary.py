# 20_localbinary.py
import cv2
import numpy as np

img = cv2.imread('./AI/images/sudoku.jpg',cv2.IMREAD_GRAYSCALE)

# 전역 자동 이진화
a, dst1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)

# 여러 부분으로 쪼개서 이진화 -> 지역 자동 이진화
dst2 = np.zeros(img.shape,np.uint8)     # 0으로 채운 이미지 만듦 -> 검은 이미지
bw = img.shape[1] // 4      # 너비를 4등분
bh = img.shape[0] // 4      # 높이를 4등분

for y in range(4):
    for x in range(4):
        img_ = img[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)


cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()