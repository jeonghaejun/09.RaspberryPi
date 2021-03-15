import picamera
import time
from vutil import *

# PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.resolution = get_resolution()
    camera.start_preview()

    for i in range(5):
        time.sleep(5)
        camera.capture(format('/home/pi/iot_workspace/picamera/data/image{}.jpg', i))

    camera.stop_preview()
