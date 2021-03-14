from gpiozero import Button, LED

button = Button(12)
led = LED(21)

while True:
    if button.is_pressed:
        # print("Button is pressed")
        led.on()
    else:
        # print("Button is not pressed")
        led.off()