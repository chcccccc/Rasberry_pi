from bmp280 import BMP280
from smbus import SMBus
from time import sleep

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
from waveshare_OLED import OLED_0in96
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)
import subprocess

#폰트 경로 설정
picdir = "/home/pi/oled/OLED_Module_Code/RaspberryPi/python/pic"  # 유니코드 지원 폰트

font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)

#disp 객체 할당
disp = OLED_0in96.OLED_0in96()
disp.Init()
disp.clear()

while True:
    disp.clear()

    # 리눅스 명령어 실행
    result = subprocess.run(['date', '+"%T"'], capture_output=True, text=True)

    #이거 매일 새로 안해주면 값 바뀌었을때 text를 똑같은 위치에 다시 쓰면서, 글자가 겹치기 시작함.
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)

    temp = bmp280.get_temperature()
    pres = bmp280.get_pressure()
    
    time = 'PM' + str(result.stdout)
    a = '현재 온도: {:05.2f}oC'.format(temp)

    draw.text( (20,0), time, font=font1,fill=0 )
    draw.text( (15,24), a ,font=font2,fill=0 )

    disp.ShowImage(disp.getbuffer(image1))
    sleep(1)