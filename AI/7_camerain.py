import cv2
import sys

cap = cv2.VideoCapture(0)  # 웹캠 사용

if not cap.isOpened():
    print('❌ 웹캠 연결 실패')
    sys.exit()
print('✅ 웹캠 연결 성공')

print('가로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('FPS: ', cap.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()