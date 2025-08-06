import cv2

# HSV
# 색을 표현하는 한 방식으로 이미지 처리와 색상 추출에서 매우 자주 사용되는 장점을 갖음
# H : 색상(빨강, 초록, 파랑 등 0~179가지를 갖고있음)
# S : 채도(색의 선명함, 0~255)
# V : 명도(밝기, 0~255)

img = cv2.imread('./AI/images/candies.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

''' 색상 H 값 (OpenCV 기준)
빨강 (Red) 0 또는 179 
주황 (Orange) 10~20
노랑 (Yellow) 20~30 
초록 (Green) 40~85
파랑 (Blue) 90~130
보라 (Violet) 130~160

채도: 150 ~ 255
명도: 0 ~ 255
'''

dst = cv2.inRange(hsv,(90,150,0),(130,255,255))
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()