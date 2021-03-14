# 동영상에서 사람 영역 추출

import cv2
import sys

face_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture("./data/vtest.avi")

if cap.isOpened():
    print('width: {}, heigth: {}' .format(cap.get(3), cap.get(4)))
else:
    print("No Camera")

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 사람 검출
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

        cv2.imshow('video', frame)

        if cv2.waitKey(1) == 27: break  # esc 키
    else:
        break

cap.release()
cv2.destroyAllWindows()