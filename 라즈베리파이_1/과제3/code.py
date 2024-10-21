from gpiozero import LED
from time import sleep

red = LED(14)
blue = LED(15)
yellow = LED(18)

toggle_1 = False
toggle_2 = False
toggle_3 = False

while(1):
    i = int(input("input >>"))
    if(i == 1):
        toggle_1 = not toggle_1
        if(toggle_1):
            red.on()
        else:
            red.off()
    elif(i == 2):
        toggle_2 = not toggle_2
        if(toggle_2):
            blue.on()
        else:
            blue.off()
    elif(i == 3):
        toggle_3 = not toggle_3
        if(toggle_3):
            yellow.on()
        else:
            yellow.off()

