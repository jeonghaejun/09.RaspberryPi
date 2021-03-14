import cv2
import numpy as np

img = cv2.imread('./data/testimg.jpg')
width = 200
height = 200

# 슬라이싱의 차원 y:x
cropImage = img[200:200+height, 200:200+width]
img[0:height, 0:width] = cropImage

# pt1 = 200, 200
# pt2 = 200+width, 200+height
# cv2.rectangle(img, pt1, pt2, (255, 0, 0), 2)
cv2.rectangle(img, (200, 200), (200+width, 200+height), (255, 0, 0), 2)
# 좌표 (x, y)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
