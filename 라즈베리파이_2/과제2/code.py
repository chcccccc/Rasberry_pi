from gpiozero import LED, Button
from signal import pause


btn = Button(14)
lazer = LED(15)

turn = True

def btn_callback():
    print("눌림!")
    global turn
    if(turn == True):
        turn = False
    else:
        turn = True

btn.when_pressed = btn_callback

while(1):
    print(turn)
    if turn == True:
        lazer.on()
    else:
        lazer.off()
pause()