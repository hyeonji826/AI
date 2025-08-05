import cv2
import numpy as np

oldx = oldy = 0  # 이전 좌표 초기화

# flag : 눌렀는지 떼졌는지 체크해주는 매개변수
def on_mouse(event,x,y,flags,param):
    # local로 하면 에러남
    global oldx, oldy
    # print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어요: %d, %d' %(x,y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떼졌어요: %d, %d' %(x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스가 이동하고있어요: %d, %d' %(x,y))
        if flags:
            print('드래그중이예요🔥: %d, %d' %(x,y))
            cv2.line(img,(oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
            # 이전 좌표 업데이트
            oldx, oldy = x, y


img = np.ones((500,500,3), dtype=np.uint8) * 255  # 흰색 배경
cv2.namedWindow('img')

cv2.rectangle(img,(50,200,150,100),(0,255,0),3) 
cv2.rectangle(img,(300,200,150,100),(0,255,0),-1) 

cv2.circle(img,(250,400),50,(255,0,0),3)

cv2.putText(img, 'Hello', (50, 300), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,0))

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey(0)