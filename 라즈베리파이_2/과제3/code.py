from gpiozero import LED
from time import sleep

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)
dp = LED(21)

fnd = [a,b,c,d,e,f,g,dp]

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

while(1):
    num = input()

    for i in num:
        to_be_turned_led = arr[int(i)] #0을 가르킴
        for j in to_be_turned_led:
            j.on()

        sleep(0.3)
        for j in to_be_turned_led:
            j.off()
        sleep(0.3)

