from microbit import *

while True:
    display.show(Image.ASLEEP)
    if accelerometer.is_gesture("shake"):
        display.show(Image.ANGRY)
        sleep(5000)
