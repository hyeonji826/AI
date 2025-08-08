import cv2
import pytesseract
import numpy as np

img = cv2.imread('./AI/images/businesscard.jpg')

dw, dh = 700,400
srcQuad = np.array([[0,0],[0,0],[0,0],[0,0]],np.float32)
dstQuad = np.array([[0,0],[0,dh],[dw,dh],[dw,0]],np.float32)
dst = np.zeros((dh,dw),np.uint8)

src_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(src_bin,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cpy = img.copt()
for pts in contours:
    if cv2.contourArea(pts) < 500:
        continue

    approx = cv2.approxPolyDP(pts,cv2.arcLength(pts,True)*0.02, True)
    cv2.polylines(cpy,[approx],True,(0,255,0),2)