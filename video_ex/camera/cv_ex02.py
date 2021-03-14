import cv2

image_file = './data/testimg.jpg'
img = cv2.imread(image_file)

cv2.imwrite('./data/testimg.bmp', img)
cv2.imwrite('./data/testimg.png', img)
cv2.imwrite('./data/testimg2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/testimg2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])