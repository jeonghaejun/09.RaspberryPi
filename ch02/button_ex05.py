from gpiozero import Button, LED
from signal import pause

button = Button(12)
led = LED(21)

led.source = button.value

pause()