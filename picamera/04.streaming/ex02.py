# LED와 PIR 센서를 연결
# 움직임이 감지되면 동영상 녹화 시작, 서버로 이미지 전송
# 움직임이 없어지면 동영상 녹화 중지, 이미지 전송 중지
# 파일명은 날짜_녹화시작시간.h264
# 화면 출력은 없음

from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep
import picamera
import datetime
import socket
import io
import json
import net

HOST = '192.168.0.4'
PORT = 5000

motion = MotionSensor(22)
led = LED(21)

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.vflip = True


def start_record():
    led.on()
    now = datetime.datetime.now()
    fname = now.strftime("%Y%m%d_%H%M")+'.h264'
    camera.start_recording(fname)
    print('recording ', fname)


def stop_record():
    led.off()
    print('recording off')
    camera.stop_recording()


motion.when_motion = start_record  # 움직임이 감지된 경우 호출할 함수
motion.when_no_motion = stop_record  # 움직임이 사라졌을 경우 호출할 함수

pause()
