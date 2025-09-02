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
dst1 = cv2.warpAffine(img,aff,(0,0))

# interpolation(보간법) : 픽셀을 어떻게 채울지 결정
# INTER_NEAREST : 최근법 이웃 보간(속도 빠름, 품질 낮음), 가까운 픽셀 값을 그대로 복사. 
# 단점 - 계산 현상이나 노이즈가 생길 수 있음
dst2 = cv2.resize(img,(1280,1024),interpolation=cv2.INTER_NEAREST) 

# INTER_CUBIC : 4차 보간법(속도 느림, 품질 좋음), 주변 16개 픽셀을 이용하여 곡선으로 예측, 이미지를 부드럽게 확대/축소
dst3 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

# center point 가져오기
cp = (img.shape[1]/2,img.shape[0]/2)
# affine 행렬을 얻을 수 있음 (30도, 0.7스케일)
rot = cv2.getRotationMatrix2D(cp, 30, 0.7)
dst4 = cv2.warpAffine(img, rot, (0, 0))

cv2.imshow('img',img)
# cv2.imshow('dst1',dst1)
# cv2.imshow('dst2',dst2)
# cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()