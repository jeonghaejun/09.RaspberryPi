import cv2

cap = cv2.VideoCapture(0)       # 1 번 카메라

while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval: break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)   # 1000/25 --> 40
    if key == 27: break     # esc키를 누른 경우 루프 탈출 (아스키코드 27번)

if cap.isOpen():
    cap.release()       # cap을 닫아줌.

cv2.destroyAllWindows()