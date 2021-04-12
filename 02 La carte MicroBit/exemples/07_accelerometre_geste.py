from microbit import *

while True:
    if accelerometer.is_gesture("shake"):
        display.show(Image.SURPRISED)