from gpiozero import Button, LED
from signal import pause

button = Button(12)

def say_hello():
    print("Hello")

button.when_pressed = say_hello

pause()