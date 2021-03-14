from gpiozero import Button, LED
from signal import pause


button = Button(12)
led = LED(21)

def say_goodbye():
    print("goodbye!")
    led.off()

def say_hello():
    print("Hello")
    led.on()




button.when_pressed = say_hello        
button.when_released = say_goodbye

pause()