from gpiozero import LED

red = LED(21)

while True:
    x = input("LED on/off : ")
    if(x == 'q'):
        break

    red.value = int(x)