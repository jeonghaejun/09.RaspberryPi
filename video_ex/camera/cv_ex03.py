# http://192.168.0.17:4747/video

import cv2

# cap = cv2.VideoCapture(0)   # 0번 카메라
cap = cv2.VideoCapture('http://haejunpi:8000/mjpeg/stream')  # ip 카메라
# cap = cv2.VideoCapture('http://192.168.0.17:4747/video?320x240')  # ip 카메라 해상도조절
# cap = cv2.VideoCapture('./data/vtest.avi')  # 동영상 파일

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval:
        break

    # 이미지(frame) 처리 -- 주로 AI와 연계

    cv2.imshow('frame', frame)
    key = cv2.waitKey(30)  # 1000/33 --> 30 fps
    if key == 27: # ESC키를 누른 경우 루프 탈출
        break  

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()
