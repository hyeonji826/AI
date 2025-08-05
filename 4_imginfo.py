import cv2
import numpy as np

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)

# adarray
print('img_gray type:', type(img_gray))
# 세로 가로
print('img_gray shape:', img_gray.shape)
# uint8 부호 없는 0~255   
print('img_gray dtype:', img_gray.dtype)

img_color = cv2.imread('./images/dog.bmp')

print('img_color type:', type(img_color))
print('img_color shape:', img_color.shape)  # 세로 가로 색상
print('img_color dtype:', img_color.dtype)

h,w = img_gray.shape[:2]
print(f'이미지 사이즈: {w}x{h}')

if len(img_gray.shape) == 3:
    print('컬러 영상')
elif len(img_gray.shape) == 2:
    print('흑백 영상')

img1 = np.zeros((240,320,3), dtype=np.uint8) 
    
# for x in range(h):
#     for y in range(w):
#         img_color[x, y] = (255,102,255)

# 전체 픽셀을 (255, 102, 255)로 변경
img1[:,:] = (255, 102, 255)  


cv2.imshow('img_color', img_color)
cv2.waitKey()