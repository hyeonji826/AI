import cv2
import sys

cap = cv2.VideoCapture(0)  # 웹캠 사용

if not cap.isOpened():
    print('❌ 웹캠 연결 실패')
    sys.exit()
print('✅ 웹캠 연결 성공')