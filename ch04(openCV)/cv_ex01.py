#/usr/bin/python
import cv2

image_file = './data/doggy.jpg'
img = cv2.imread(image_file)    # cv2.IMREAD_COLOR
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape)    # 512x512x3 byte
print(img.dtype, img2.dtype)    # 512x512 byte

cv2.imshow('doggy color', img)
cv2.imshow('doggy grayscale', img2)

cv2.waitKey(0)          # 키 입력 대기, 인자는 시간(ms), 0이면 무한 대기, 키코드 값이 리턴
cv2.destroyAllWindows() # 출력한 모든 창 닫기

