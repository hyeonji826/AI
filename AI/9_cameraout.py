import cv2

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f'웹캠 해상도: {w}x{h}, FPS: {fps}')
fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('camera.avi', fourcc, fps, (w, h))

while True:
    ret,frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('camera', frame)
    if cv2.waitKey(10) == 27:  # ESC 키로 종료
        break

cap.release()
out.release()