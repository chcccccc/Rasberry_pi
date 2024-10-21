from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep


#잘자라 우리아가,,
lst = [329.62, 369.99, 329.62, 293.66, 261.62,  293.66, 261.62]

b = TonalBuzzer(14)

while True:
    for i in range(len(lst)):
        b.play(lst[i])
        sleep(0.4)
    b.stop()
    break