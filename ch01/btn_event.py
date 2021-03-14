import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print("Button pushed")

button_pin = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button_pin, GPIO.RISING, 
                    callback=button_callback, bouncetime = 200)

try:
	while 1:
		time.sleep(0.1)
finally:
	GPIO.cleanup()
