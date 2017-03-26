from microbit import *
f = 9
o = 0
while True:
    display.set_pixel(2,0,f)
    display.set_pixel(1,1,f)
    display.set_pixel(2,1,f)
    display.set_pixel(3,1,f)
    display.set_pixel(2,2,f)
    display.set_pixel(1,3,f)
    display.set_pixel(3,3,f)
    display.set_pixel(1,4,f)
    display.set_pixel(3,4,f)
    sleep(1000)
    display.clear()
    display.set_pixel(2,0,f)
    display.set_pixel(1,1,f)
    display.set_pixel(2,1,f)
    display.set_pixel(3,1,f)
    display.set_pixel(2,2,f)
    display.set_pixel(2,3,f)
    display.set_pixel(2,4,f)
    sleep(1000)
    display.clear()