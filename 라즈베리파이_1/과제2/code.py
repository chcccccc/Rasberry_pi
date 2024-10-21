from gpiozero import LED
from time import sleep


red = LED(14)

time = 1
while(time >= 0.1):
    red.on()
    sleep(0.1)
    red.off()
    sleep(time)
    time *= 0.9
