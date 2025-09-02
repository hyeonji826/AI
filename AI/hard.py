import cv2
import numpy as np

img = cv2.imread('./AI/images/namecard.jpg')
orig = img.copy()

drag_idx  = -1
r = 15
color_circle = (100, 100, 255)    
color_line   = (0, 0, 0)   
th= 2

pts = [
    (30,30),   
    (700,30),   
    (700,768),   
    (30,768),  
]

for (oldx,oldy) in pts:
    cv2.circle(img,(oldx,oldy),r,color_circle,-1)

cv2.line(img, pts[0], pts[1], color_line, th)  
cv2.line(img, pts[1], pts[2], color_line, th)  
cv2.line(img, pts[2], pts[3], color_line, th)  
cv2.line(img, pts[3], pts[0], color_line, th) 

def on_mouse(event,x,y,flags,param):
    global drag_idx, img, pts
    
    # 드래그
    if event == cv2.EVENT_LBUTTONDOWN:
        for i,(px,py) in enumerate(pts):
            if(x-px)**2 + (y-py)**2 <= r**2:
                drag_idx = i
                break
    elif event == cv2.EVENT_MOUSEMOVE and drag_idx != -1:
        pts[drag_idx] = [x,y]
        img = orig.copy()
        for (newx,newy) in pts:
            cv2.circle(img,(newx,newy),r,color_circle,-1)
        cv2.line(img, pts[0], pts[1], color_line, th)  
        cv2.line(img, pts[1], pts[2], color_line, th)  
        cv2.line(img, pts[2], pts[3], color_line, th)  
        cv2.line(img, pts[3], pts[0], color_line, th)
        
    elif event == cv2.EVENT_LBUTTONUP:
        drag_idx = -1
           
           
cv2.namedWindow('img')
cv2.setMouseCallback('img',on_mouse)
while True:
    cv2.imshow('img', img)
    if cv2.waitKey(0) == 27: 
        break