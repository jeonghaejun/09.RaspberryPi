import cv2
import numpy as np

img = cv2.imread('./data/testimg.jpg')
# img = cv2.imread('./data/testimg.jpg', cv2.IMREAD_GRAYSCALE)

print('img.dmin=', img.ndim)
print('img.shape=', img.shape)
print('img.dtype=', img.dtype)

# np.bool, np.uint16, np.unit32, np.float32, np.float64, np.complex64
img = img.astype(np.int32)
print('img.dtype=', img.dtype)

img = np.uint8(img)
print('img.dtype=', img.dtype)
