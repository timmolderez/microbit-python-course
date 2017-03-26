from microbit import *

# Start calibrating
if not compass.is_calibrated():
    compass.calibrate()

# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)
    needle = ((15 - compass.heading()) // 45) % 8
    display.show(Image.ALL_ARROWS[needle])