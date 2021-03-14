from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(13, 19, max_distance=1, threshold_distance=0.2) # echo, trig
led = LED(21)

sensor.when_in_range = led.off
sensor.when_out_of_range = led.on

pause()