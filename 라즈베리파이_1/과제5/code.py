from gpiozero import LED, Button
from time import sleep

led_pin = [14,15,18,23]
leds = [LED(i) for i in led_pin]

btn1 = Button(17)
btn2 = Button(27)

index = -1

while(1):
    if(btn1.is_pressed):
        leds[index].off()
        index += 1
        index = index % 4
        leds[index].on()
        sleep(0.3)
        
    elif (btn2.is_pressed):
        print("reset 눌림!")
        leds[index].off()
        index = -1
    