# ROI(Region of Interest) : 관심 영역
import cv2
import numpy as np

img = cv2.imread('./AI/images/sun.jpg')
img_backup = img.copy()

x = 182
y = 22
w = 119
h = 108

roi = img[y:y+h, x:x+w]
# roi_copy = roi.copy()
# img[y:y+h, x+w:x+w+w] = roi

# 두 태양을 박스로 감싸기
# cv2.rectangle(img,(x, y),(x+w+w, y+h),(0,255,0),2)

# cv2.imshow('img',img)
# cv2.waitKey()

oldx = oldy = 0

def on_mouse(event,x,y,flags,param):
    global oldx, oldy ,img
    if event == cv2.EVENT_LBUTTONDOWN:
        print('%d, %d' %(x,y))
        oldx, oldy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        img = img_backup.copy()
        cv2.rectangle(img, (oldx, oldy), (x, y), (0,255,0), 3)
        cv2.imshow('img', img)
    elif event == cv2.EVENT_LBUTTONUP:
        endx, endy = x, y
        x1, x2 = sorted([oldx, endx])
        y1, y2 = sorted([oldy, endy])
        
        roi = img_backup[y1:y2, x1:x2]
        cv2.imshow('ROI', roi)
        cv2.imwrite('cropped_box.png', roi)

        img = img_backup.copy()
        cv2.imshow('img', img)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)
cv2.imshow('img', img)
cv2.waitKey(0)