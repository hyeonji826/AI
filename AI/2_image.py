import cv2

img1 = cv2.imread('./images/dog.bmp',cv2.IMREAD_GRAYSCALE)
# print(img1)

# 기본값이 컬러
img2 = cv2.imread('./images/dog.bmp')
# print(img2)

# 윈도우에서 새창이 열려서 이미지를 보여줌
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)  # 키 입력을 기다림