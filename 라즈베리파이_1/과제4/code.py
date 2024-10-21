from gpiozero import LED, Button
from time import sleep


led_pin = [14,15,18]
leds = [LED(i) for i in led_pin]

btn1 = Button(17)
btn2 = Button(27)


def btn1_callback():
    for i in range(3):
        for j in range(3):
            leds[j].on()
            sleep(0.5)
            leds[j].off()

def btn2_callback():
    for i in range(3):
        for j in range(3):
            leds[j].on()
        sleep(0.5)
        for j in range(3):
            leds[j].off()
        
        sleep(0.5)


while(1):
    if(btn1.is_pressed):
        print("btn1 눌림")
        btn1_callback()
    elif(btn2.is_pressed):
        print("btn2 눌림")
        btn2_callback()
