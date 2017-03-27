from microbit import *

lost = False
while not lost:
    if accelerometer.get_x() > 400 or accelerometer.get_x() < -400:
        lost = True
    if accelerometer.get_y() > 400 or accelerometer.get_y() < -400:
        lost = True
    
display.show(Image.SKULL)