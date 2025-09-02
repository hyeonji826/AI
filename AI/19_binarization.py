# 19_binarization.py

# 이진화
# 이미지의 픽셀 값을 0과 1(0과 255) 두 가지 값만 가지도록 만드는 영상 처리 기법
# OCR, 윤곽 검출, 객체 분할, 문서 스캔 등 작업에 유리

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./AI/images/cells.png',cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img],[0],None,[256],[0,255])

# 픽셀값이 임계값을 넘으면 최대값으로 설정하고, 넘지 못하면 0으로 지정
a,dst1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
print(a)    # 100.0
# 임계값 수정
b,dst2 = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
print(b)    # 210.0
# 오츠 이진화
c,dst3 = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(c)    # 206.0 -> 자동 임계값

# 오츠 이진화의 단점?
# 이미지를 전체적으로 본 후 임계값을 찾아내는데, 이는 이미지 픽셀의 평균을 내서 값을 찾는다고 예상할 수 있다. 따라서 밝고 어두우면 잘 못찾을 수 있다.


cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
plt.plot(hist)
plt.show()
cv2.waitKey()