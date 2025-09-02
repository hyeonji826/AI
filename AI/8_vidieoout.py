import cv2

# 첫번째 영상 뒤에 두번째 영상을 이어붙이기
cap1 = cv2.VideoCapture('./AI/movies/dog.mp4')
cap2 = cv2.VideoCapture('./AI/movies/cat.mp4')
# 단, 해상도가 같아야함

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

print(f'첫번째 영상: {w}x{h}, {frame_cnt1}프레임, FPS: {fps1}')
print(f'두번째 영상: {w}x{h}, {frame_cnt2}프레임, FPS: {fps2}')

# VideoWriter : 동영상을 만드는 객체
# png, mp4v, DIVX(avi 방식) etc.. : 압축방식
fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))

for i in range(frame_cnt1):
    ret, frame = cap1.read()
    cv2.imshow('ouput',frame)
    # 파일에 내용을 저장
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break
    
for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('ouput',frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break
    
cap1.release()
cap2.release()
out.release()