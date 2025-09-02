import cv2
import sys

cap = cv2.VideoCapture('./AI/movies/dog.mp4')

if not cap.isOpened():
    print('❌ 동영상을 불러올 수 없음')
    sys.exit()
print('✅ 동영상을 불러올 수 있음')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
print(f'프레임 크기: {width}x{height}')
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(f'총 프레임 개수 : {frame_count}')
fps = cap.get(cv2.CAP_PROP_FPS)
print(f'FPS: {fps}') 

while True:
    # 프레임 한장 가져옴
    # frame : numpy.ndarray
    # ret : Trie/False
    ret, frame = cap.read()
    if not ret:
        break  
    cv2.imshow('frame', frame)
    # 안에 숫자는 m/s
    if cv2.waitKey(10) == 27:
        break

# 프로그램상 리소스를 많이 쓰는건 release()로 해제
cap.release() 