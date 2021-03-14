# 동영상에서 얼굴 영역 추출

import cv2
import numpy as np
import time

face_classifier = cv2.CascadeClassifier(
    './face/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# cap.get(cv2.CAP_PROP_POS_FRAMES)
# cap.get(cv2.CAP_PROP_FRAME_COUNT)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) (3)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) (4)

if cap.isOpened():
    print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))
else:
    print("No Camera")

while True:
    start_time = time.time()
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 얼굴 검출
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cropped_face = frame[y:y+h, x:x+w].copy()
            cropped_face = cv2.resize(cropped_face, dsize=(
                300, 300), interpolation=cv2.INTER_AREA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

            cv2.imshow('face', cropped_face)
        cv2.imshow('video', frame)

        if cv2.waitKey(1) == 27:
            break  # ESC 키
    else:
        print('error')

    # fps(frame per second) 계산
    end_time = time.time()
    fps = 1 / (end_time-start_time)
    print(f'fps: {fps}')

cap.release()
cv2.destroyAllWindows()
