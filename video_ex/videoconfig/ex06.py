import cv2
src = cv2.imread('./data/testimg.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # ***** 사용빈도 높음
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
rgb=cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # ***** 사용빈도 높음, 다른 라이브러리 연동시

cv2.imshow('gray', gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv', hsv)
cv2.imshow('rgb', rgb)


cv2.waitKey()
cv2.destroyAllWindows()
