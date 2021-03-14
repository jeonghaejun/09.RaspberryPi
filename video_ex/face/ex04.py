# 영상에서 사람을 찾아서 사각형 표시

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('./face/haarcascade_fullbody.xml')
cap = cv2.VideoCapture('./data/vtest.avi')  # 동영상 파일

if cap.isOpened():
    print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))
else:
    print("No Camera")

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        

        # 사람 검출
        bodies = face_classifier.detectMultiScale(gray, 1.3, 5, minSize=(10,10))
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

        cv2.imshow('video', frame)
        if cv2.waitKey(1) == 27:
            break  # ESC 키
    else:
        break

cap.release()
cv2.destroyAllWindows()
