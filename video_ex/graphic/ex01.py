import cv2
import numpy as np

# White 배경 색상
img = np.zeros(shape=(512, 512, 3), dtype=np.uint8) + 255
# img = np.ones((512, 512, 3), dtype=np.uint8) * 255
# img = np.full((512, 512, 3), (255,255,255), dtype=up.uint8)

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)  # (255, 0, 0) -> 파란색 (B, G, R) <- 오픈cv이만 순서가 이렇게 된다.
cv2.line(img, (0, 0), (0, 500), (0, 0, 255), 5)  # (0, 0, 255) -> 빨간색

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
