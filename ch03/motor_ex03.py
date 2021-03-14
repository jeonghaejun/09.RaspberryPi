from gpiozero import AngularServo
from time import sleep

myGPIO = 26

servo = AngularServo(26, min_angle=-90, max_angle=90, min_pulse_width=0.0004, max_pulse_width=0.0024)   # 0~180

while True:
    servo.angle = -90
    print("mid")
    sleep(2)
    servo.angle = 0
    print("min")
    sleep(2)
    servo.angle = 90
    print("mid")
    sleep(2)
    servo.angle = 0
    print("max")
    sleep(2)
    