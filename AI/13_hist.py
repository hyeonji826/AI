import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./AI/images/candies.png', cv2.IMREAD_GRAYSCALE)

# 히스토그램
# 이미지 히스토그램 : 밝기(또는 색상)값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇개나 있는지 확인
# imgaes : 대상 이미지 리스트
# channel : 분설할 채널 번호 (B:0, G:1, R:2)
# mask : 분석할 영역 마스크 (None : 전체 이미지)
# histSize : 히스토그램의 빈 개수 (256 : 0~255까지)
# ranges : 값의 범위 (0~256)
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])

# plot 설정
plt.figure(figsize=(10,4))
plt.subplot(121)
plt.plot(hist1,color='gray')

img2 = cv2.imread('./AI/images/candies.png')
print('shape:', img2.shape)
print('dtype:', img2.dtype)

'''
b = img[:,:, 0]
g = img[:,:, 1]
r = img[:,:, 2]
'''
# b, g, r = cv2.split(img2)  # 채널 분리

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)
plt.plot(hist1)
plt.show()
cv2.waitKey()

# candies.png 영상을 컬러로 불러와 3개의 채널을 계산하여 히스토그램을 그리기
# 단, 하나의 plot에서 BGR 그래프를 모두 출력(색상을 다르게 표현)
''' 내가 한 코드
plt.figure(figsize=(10,4))
plt.subplot(122)
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([img2], [1], None, [256], [0, 256])
hist4 = cv2.calcHist([img2], [2], None, [256], [0, 256])
plt.plot(hist2, color='b')
plt.plot(hist3, color='g')
plt.plot(hist4, color='r')
plt.legend(['B', 'G', 'R'])
plt.show()
cv2.waitKey()
'''
''' 강사님 코드 '''
colors = ['b','g','r']
channels = cv2.split(img2)

plt.subplot(122)

for ch, color in zip(channels, colors):
    hist = cv2.calcHist([ch],[0],None,[256],[0,255])
    plt.plot(hist, color = color, label=color.upper())