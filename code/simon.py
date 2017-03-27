from microbit import *
import random


def showgesture(gest):
    if gest == "up":
        display.show(Image.ARROW_S)
    if gest == "down":
        display.show(Image.ARROW_N)
    if gest == "left":
        display.show(Image.ARROW_W)
    if gest == "right":
        display.show(Image.ARROW_E)


gestures = ["up", "down", "left", "right", "face up", "face down", "shake"]
gestures_simple = ["up", "down", "left", "right"]


while True:
    chosen1 = random.choice(gestures_simple)
    chosen2 = random.choice(gestures_simple)
    chosen3 = random.choice(gestures_simple)

    showgesture(chosen1)
    sleep(1000)
    showgesture(chosen2)
    sleep(1000)
    showgesture(chosen3)
    sleep(1000)
    display.clear()

    while not accelerometer.current_gesture() == chosen1:
        display.show(Image.COW)
    while not accelerometer.current_gesture() == chosen2:
        display.show(Image.BUTTERFLY)
    while not accelerometer.current_gesture() == chosen3:
        display.show(Image.GIRAFFE)
    display.show(Image.SMILE)
    sleep(3000)
