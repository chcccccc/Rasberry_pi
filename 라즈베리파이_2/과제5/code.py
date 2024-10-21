#손님이 몇명 왔는지 counting 해보기
import warnings
from gpiozero import DistanceSensor
from time import sleep

warnings.filterwarnings("ignore", category=UserWarning, module='gpiozero')

sensor = DistanceSensor(echo=15, trigger=14)
pcount = 0
while True:
    print(pcount,"명 왔다감")
    if(sensor.distance <= 0.3) :
        pcount += 1
        print("한명 추가!")
    
    sleep(0.3)
    