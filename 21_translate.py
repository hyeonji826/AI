import cv2
import numpy as np

img = cv2.imread('./AI/images/dog.bmp')

# 행렬 연산 후 이미지 변환
aff = np.array([
    [1,0,150],
    [0,1,100]
], dtype=np.float32)

# Affine 변환
# 이미지의 위치나 모양을 변경하는 선형변환 즉, 이미지와 행렬 연산 -> 이미지가 이동된다.
# (0,0) -> 원본 이미지 크기를 그대로 전달
dst = cv2.warpAffine(img,aff,(0,0))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()