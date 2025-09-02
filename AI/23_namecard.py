import cv2
import numpy as np
import sys

img = cv2.imread('./AI/images/namecard.jpg')
h,w = img.shape[:2]

dh = 500
# A4용지 크기 : 210mm*297mm
dw = round(dh * 297 / 210)  # 출력될 크기

# 30 픽셀씩 띄어줌
srcQuad = np.array([
    [30,30],[30,h-30],[w-30,h-30],[w-30,30]]
,np.float32)

dstQuad = np.array([
    [0,0],[0,dh],[dw,dh],[dw,0]]
,np.float32)

# 어떤게 드래그 되고있는지 알 수 있는 함수
dragSrc = [False,False,False,False]

# 예전 좌표 -> 튜플로 쓸 예정
ptOld = 0

def drawROI(img,corners):
    cpy = img.copy()
    c1 = (192,192,255)
    c2 = (128,128,255)
    
    for pt in corners:
        cv2.circle(cpy,tuple(pt.astype(int)),25,c1,-1)
    
    cv2.line(cpy,tuple(corners[0].astype(int)),tuple(corners[1].astype(int)),c2,2)
    cv2.line(cpy,tuple(corners[1].astype(int)),tuple(corners[2].astype(int)),c2,2)
    cv2.line(cpy,tuple(corners[2].astype(int)),tuple(corners[3].astype(int)),c2,2)
    cv2.line(cpy,tuple(corners[3].astype(int)),tuple(corners[0].astype(int)),c2,2)
    
    return cpy


def onMouse(event,x,y,flags,param):
    global srcQuad ,dragSrc, ptOld
    
    if event == cv2.EVENT_LBUTTONDOWN:   # 눌렀을 때
        for i in range(4):
            # srcQuad의 인덱스(원마다) 클릭이 반지름 내에서 눌린다면! -> norm 정규화
            if cv2.norm(srcQuad[i] - (x,y)) < 25:
                dragSrc[i] = True
                ptOld = (x,y)
                break
    elif event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                srcQuad[i] = (x,y)
                # 다시 그려줌
                cpy = drawROI(img,srcQuad)
                cv2.imshow('img',cpy)
                ptOld = (x,y)
                break
    elif event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False
    
    
    

disp = drawROI(img,srcQuad)
cv2.namedWindow('img')
cv2.setMouseCallback('img',onMouse)
cv2.imshow('img',disp)

while True:
    key = cv2.waitKey()
    if key ==27:
        sys.exit()
    elif key == 13:
        break

pers =cv2.getPerspectiveTransform(srcQuad,dstQuad)
dst = cv2.warpPerspective(img,pers,(dw,dh),flags=cv2.INTER_CUBIC)
cv2.imshow('dst',dst)
cv2.waitKey()