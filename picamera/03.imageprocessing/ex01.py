# numpy 배열에 저장하기

import time
from picamera import PiCamera
import numpy as np
from video import Video

with PiCamera() as camera:
    camera.vflip = True
    # camera.resolution = (320, 240)
    camera.resolution = (640, 480)
    camera.framerate = 30  # 무한정 높인다고 프레임이 올라가는게 아니다. 적정수치를 찾아야 함.

    # time.sleep(2) # 카메라 예열시간

    # output = np.empty((240, 320, 3), dtype=np.uint8)
    output = np.empty((480, 640, 3), dtype=np.uint8)

    while True:
        start_time = time.time()
        camera.capture(output, 'bgr', use_video_port=True)
        if not Video.show(output):
            break
        end_time = time.time()
        fps = 1/(end_time-start_time)
        print(f'fps: {fps}')
