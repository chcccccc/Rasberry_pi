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


from gpiozero import LED, Button
from signal import pause

btn = Button(14)
flag = 1

def btn_Callback():
    global flag
    if(flag == 1):
        flag = 2
        disp.clear()
    else:
        flag = 1
        disp.clear()

    

btn.when_pressed = btn_Callback

try:
    disp = OLED_0in96.OLED_0in96()    
    disp.Init()

    while(1):
        if(flag == 1):
            print("draw image1")

            Himage1 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
            bmp = Image.open(os.path.join(picdir, '0in96.bmp'))
            Himage1.paste(bmp, (0,0))
            Himage1=Himage1.rotate(0) 	
            disp.ShowImage(disp.getbuffer(Himage1))  


        else:
            print("draw image2")

            Himage2 = Image.new('1', (disp.width, disp.height), 255)
            png_image = Image.open(os.path.join(picdir, 'heart.png'))
            png_image = png_image.resize((128, 32))
            Himage2.paste(png_image, (0, 0))
            disp.ShowImage(disp.getbuffer(Himage2))  

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()



pause()