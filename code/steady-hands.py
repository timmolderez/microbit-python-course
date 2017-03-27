from microbit import *

while not pin0.is_touched():
    display.show(Image.HAPPY)
display.show(Image.SAD)
