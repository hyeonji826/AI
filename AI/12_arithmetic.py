import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./AI/images/dog.jpg')
img2 = cv2.imread('./AI/images/square.bmp')

dst1 = cv2.add(img1, img2)  # 단순 덧셈
# 두 이미지를 비율로 섞음
dst2 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  # 가중치 덧셈
dst3 = cv2.subtract(img1, img2)
# 두 이미지같의 절대 차이값 : abs(img1(x,y) - img2(x,y))
# 예) img1 = 80, img2 = 100 -> abs(-20) = |20|
dst4 =cv2.absdiff(img1, img2)  

img = {'dst1': dst1, 'dst2': dst2, 'dst3': dst3, 'dst4': dst4}
for i, (k,v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:,:,::-1])  # BGR -> RGB
    plt.title(k)
plt.show()