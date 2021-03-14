import cv2

image_file = './data/doggy.jpg'
img = cv2.imread(image_file)

cv2.imwrite('./data/doggy.bmp', img)
cv2.imwrite('./data/doggy.png', img)
cv2.imwrite('./data/doggy2.bmp', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/doggy2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])