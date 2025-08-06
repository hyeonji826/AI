import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./AI/images/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)
# 히스토그램 평활화
# 이미지의 전체 밝기 분포를 고르게 퍼뜨려 명암 대비를 향상시키는 기법
dst = cv2.equalizeHist(img)

hist1 = cv2.calcHist([img],[0],None,[256],[0,255])
hist2 = cv2.calcHist([dst],[0],None,[256],[0,255])

hists = {'hist':hist1, 'hist2':hist2}

cv2.imshow('img',img)
cv2.imshow('dst',dst)

plt.figure(figsize=(10,6))
for i, (k,v) in enumerate(hists.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()

cv2.waitKey()