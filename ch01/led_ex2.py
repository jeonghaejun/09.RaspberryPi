from gpiozero import LED
from signal import pause

red = LED(21)

red.blink(on_time=0.5, off_time=0.5)

pause()