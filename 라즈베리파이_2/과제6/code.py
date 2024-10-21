from gpiozero import LED, Button
from time import sleep

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)

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

while(1):
    for i in range(10):
        print(i)
        count += 1
        lights = arr[count]
        for j in lights:
            j.on()
        
        sleep(0.1)
        for j in lights:
            j.off()
        sleep(0.1)

    sleep(0.5)

    for i in range(9,-1,-1):
        lights = arr[count]
        count -= 1
        for j in lights:
            j.on()
        sleep(0.1)
        for j in lights:
            j.off()
        sleep(0.1)

    sleep(0.5)
    