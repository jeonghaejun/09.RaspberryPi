from gpiozero import Button
from signal import pause

count = 0


def say_hello():
    global count
    count += 1
    print("Hello", count)


button = Button(12)

button.when_pressed = say_hello

pause()