from gpiozero import LED, Button
from signal import pause


btn = Button(14)
lazer = LED(15)

turn = True


while(1):
    if btn.is_pressed:
        print("켜짐")
        lazer.on()
    else:
        print("꺼짐")
        lazer.off()

pause()