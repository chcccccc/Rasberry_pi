import sys
import os
sys.path.append('/home/pi/rfid/MFRC522-python/mfrc522')

from mfrc522 import SimpleMFRC522
from time import sleep
from mfrc522 import SimpleMFRC522

while True:
    print('Tag your Card!')
    id = SimpleMFRC522().read()[0]
    print(id)
    
    print('Tag your 토큰!')
    token = SimpleMFRC522().read()[0]
    print(token)
    sleep(0.3)