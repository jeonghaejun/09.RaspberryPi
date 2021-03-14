import cv2

# cap = cv2.VideoCapture("http://192.168.219.103:4747/video?800x600")       # 1 번 카메라
cap = cv2.VideoCapture("./data/vtest.avi")  # 동영상 파일

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)


while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval: break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(30)   
    if key == 27: break     # esc키를 누른 경우 루프 탈출 (아스키코드 27번)

if cap.isOpen():
    cap.release()       # cap을 닫아줌.

cv2.destroyAllWindows()

# http://192.168.219.103:4747/video