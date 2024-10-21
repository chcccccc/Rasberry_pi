from gpiozero import LED, Button
from time import sleep
from signal import pause


led_pin = [14,15,18,23]
leds = [LED(i) for i in led_pin]

#polling = while문으로 계속 확인하고 있는거
#interrupt = 듣고있다가 호출하는거!


mode = 1
toggle = False
button = Button(27)

def changeMode():
    global mode
    print("눌림!")
    if(mode == 2):
        mode = 1
    else:
        mode = 2

button.when_pressed = changeMode

while(1):
    print(mode)
    if(mode == 1):
        toggle = not toggle
        if(toggle):
            print("짝")
            for i in range(len(led_pin)):
                if(i % 2 == 0):
                    leds[i].on()
                else:
                    leds[i].off()
            sleep(0.1)
        else:
            print("홀")
            for i in range(len(led_pin)):
                if(i % 2 == 0):
                    leds[i].off()
                else:
                    leds[i].on()
            sleep(0.1)  
            
    else:
        for i in range(len(led_pin)):
            leds[i].on()

        sleep(0.3)
        for i in range(len(led_pin)):
            leds[i].off()
    
    sleep(0.3)

        
    
pause()


