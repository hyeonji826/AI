import cv2
import numpy as np

cap1 = cv2.VideoCapture('./AI/movies/run.mp4')
cap2 = cv2.VideoCapture('./AI/movies/woman.mp4')

w = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))

while True:
    ret1, bg = cap1.read()
    ret2, fg = cap2.read()
    if not (ret1 and ret2):
        break

    hsv = cv2.cvtColor(fg,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(40,150,0),(130,255,255))
    mask_inv = cv2.bitwise_not(mask)
    fg_person = cv2.bitwise_and(fg, fg, mask=mask_inv)
    bg_region = cv2.bitwise_and(bg, bg, mask=mask)
    composite = cv2.add(fg_person, bg_region)

    out.write(composite)
    cv2.imshow('Composite', composite)
    if cv2.waitKey(1)== 27:
        break

cap1.release()
cap2.release()
out.release()
