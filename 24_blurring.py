import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./AI/images/dog.bmp')
dst1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# (7,7) : 커널 사이즈(필터 사이즈)
dst2 = cv2.blur(img, (7, 7))
dst3 = cv2.GaussianBlur(img, (0, 0), 2)
dst4 = cv2.medianBlur(img,3)

# cv2.imshow('img', img)
# cv2.imshow(' 1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)


plt.figure(figsize=(10, 5))
for i, k in enumerate([5, 7, 9]):
    # k*k 크기 커널 생성 : 예) k=5, 1/25로 채워진 5*5 행렬
    kernel = np.ones((k, k)) / k ** 2
    # dst1 : 영상
    # -1 : 출력 이미지의 채널을 동일하게
    filtering = cv2.filter2D(dst1, -1, kernel)
    plt.subplot(1, 3, i+1)
    plt.imshow(filtering)
    plt.title('kernel size: {}'.format(k))
    plt.axis('off')
    
plt.show()
cv2.waitKey()