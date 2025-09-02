import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./AI/images/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)
# 히스토그램 평활화
# 이미지의 전체 밝기 분포를 고르게 퍼뜨려 명암 대비를 향상시키는 기법
# 이건 그레이스케일에서밖에 안쓰임
dst1 = cv2.equalizeHist(img1)

img2 = cv2.imread('./AI/images/field.bmp')
# BGR -> YCrCb
# YCrCb : 색공간
# Y : 밝기(명도)
# Cr : 빨강 계열 색상 정보 , Cb : 파란계열 색상 정보
dst2 = cv2.cvtColor(img2,cv2.COLOR_BGR2YCrCb)
ycrcb = cv2.split(dst2) # 분리
ycrcb = list(ycrcb) # 리스트화
ycrcb[0] = cv2.equalizeHist(ycrcb[0])
dst2 = cv2.merge(ycrcb)
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)

# img1 : 원본 이미지 또는 배열
# None : 출력 배열(None이면 새로 생성)
# 0 : 정규화 후 최소값 
# 255 : 정규화 후 최대값
# cv2.NORM_MINMAX : 정규화 방식
dst3 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX)

hist1 = cv2.calcHist([img1],[0],None,[256],[0,255])
hist2 = cv2.calcHist([dst1],[0],None,[256],[0,255])
hist3 = cv2.calcHist([dst3],[0],None,[256],[0,255])

hists = {'hist':hist1, 'hist2':hist2, 'hist3':hist3}

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)


plt.figure(figsize=(10,6))
for i, (k,v) in enumerate(hists.items()):
    plt.subplot(1, 3, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()

cv2.waitKey()

# split() -> merge()를 사용하지 않고 슬라이싱과 인덱싱을 이용하여 위 예제와 동일하게 결과 영상을 만들어보자
''' 내가 한 코드
b = img2[:,:, 0]
g = img2[:,:, 1]
r = img2[:,:, 2]
b, g, r = cv2.split(img2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
img_color = cv2.merge([b, g, r])

cv2.imshow('Merged Color', img_color)
cv2.waitKey()
'''

dst2[:,:,0] = cv2.equalizeHist(dst2[:,:,0])
dst2 = cv2.cvtColor(dst2,cv2.COLOR_YCR_CB2BGR)