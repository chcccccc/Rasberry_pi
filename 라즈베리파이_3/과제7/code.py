import sys
import os
from gpiozero import LED
from time import sleep

sys.path.append('/home/pi/rfid/MFRC522-python/mfrc522')
from mfrc522 import SimpleMFRC522

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

led1 = LED(14)
led2 = LED(15)

lfid_gpio = [8,11,10,9,25]
count = 0 #출입인원수

def Success():
    global count
    print("Welcome!")
    count += 1
    on_LED()

def Fail():
    print("로그인 실패")
    for i in range(5):
        led2.on()
        sleep(0.1)
        led2.off()
        sleep(0.1) 

def on_LED():
    #i = 3,4,5,6...
    for i in str(count): 
        #3에 필요한 애들
        print(i)
        to_turn_leds = arr[int(i)]
        for j in to_turn_leds:
            j.on()
        sleep(0.3)
        for j in to_turn_leds:
            j.off()
        
        sleep(0.3)


#시스템 시작
#준비
print("Ready")
print("ON")

for i in range(3):
    led1.on()
    sleep(0.5)
    led1.off()
    sleep(0.5)
led1.on()

#비밀번호 입력
in_pw = ""
while(in_pw == ""):
    print("출입증을 등록하세요: ")
    try:
        in_pw = SimpleMFRC522().read()[0]
        print("정상적으로 등록됐습니다")
        break
    except Exception as e:
        in_pw = ""

#출입 시스템 작동중
while(1):
    pw = SimpleMFRC522().read()[0]
    if(in_pw == pw):
        Success()
    else:
        Fail()


