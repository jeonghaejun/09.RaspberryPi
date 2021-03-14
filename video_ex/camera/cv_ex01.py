import cv2

image_file = './data/testimg.jpg'
img = cv2.imread(image_file)  # cv2.IMREAD_COLOR
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape)    # 772x746x3 byte
print(img.dtype, img2.dtype)    # 772x746 byte

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey(0)             # 키 입력 대기, 인자는 시간(ms), 0이면 무한 대기
cv2.destroyAllWindows()    # 출력한 모든 창 닫기