import RPi.GPIO as GPIO
import time

button_pin = 20
led_pin = 21

GPIO.setmode(GPIO.BCM)


# GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

try:
	while 1:
		# if GPIO.input(button_pin) == GPIO.HIGH:
		if GPIO.input(button_pin) == GPIO.LOW:
			print("Button pushed!")
			GPIO.output(led_pin,1)
		else:
			GPIO.output(led_pin,0)
		time.sleep(0.1)
finally:
	GPIO.cleanup()
