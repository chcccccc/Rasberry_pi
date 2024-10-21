from gpiozero import LED
from time import sleep


red = LED(14)

while True:
    red.on()
    sleep(0.1)
    red.off()
    sleep(0.5)
