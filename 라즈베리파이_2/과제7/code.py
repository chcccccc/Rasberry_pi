from gpiozero import LED, Button
from time import sleep
from signal import pause
from threading import Timer

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)

btn = Button(2)
lazer = LED(23)

led1 = LED(1)
led2 = LED(12)


arr = [
    [a,b,c,d,e,f], #0
    [b,c], #1
    [a,b,g,e,d], #2
    [a,b,g,c,d], #3
    [f,g,b,c], #4
    [a,f,g,c,d], #5
    [a,c,d,e,f,g], #6
    [f,a,b,c], #7
    [a,b,c,d,e,f,g], #8 
    [a,b,c,d,f,g], #9
]

count = -1
stop_event = False

def btnPress():
    global count
    global stop_event
    print(count,"에 눌림!")
    if(count == 7):
        #3초동안 깜빡이기
        end_time = Timer(3, stop_blinking)  # 3초 후에 깜박이는 것을 멈춤
        end_time.start()

        while not stop_event :
            lazer.on()
            led1.on()
            led2.on()
            sleep(0.3)

            lazer.off()
            led1.off()
            led2.off()
            sleep(0.3)

        stop_event = False

def stop_blinking():
    global stop_event
    stop_event = True

btn.when_pressed = btnPress

while(1):
    for i in range(10):
        print(i)
        count += 1
        lights = arr[count]
        for j in lights:
            j.on()
        
        sleep(0.3)
        for j in lights:
            j.off()
        sleep(0.3)

    sleep(0.5)

    for i in range(9,-1,-1):
        print(i)
        lights = arr[count]
        count -= 1
        for j in lights:
            j.on()
        sleep(0.3)
        for j in lights:
            j.off()
        sleep(0.3)

    sleep(0.5)

