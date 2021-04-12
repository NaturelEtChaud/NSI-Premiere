from microbit import *
from random import randint

nbSix = 0
while True:
    display.show(Image.ASLEEP)
    if accelerometer.was_gesture("shake"):
        de = randint(1, 6)
        if de == 6:
            nbSix = nbSix + 1
            if nbSix == 1:
                display.show(Image.HAPPY)
            else:
                display.show(Image.SKULL)

        else:
            display.show(str(de))
            nbSix = 0
        sleep(1500)