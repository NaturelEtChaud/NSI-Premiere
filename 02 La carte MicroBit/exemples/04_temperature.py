from microbit import *

while True:
    display.scroll(str(temperature()))
    display.scroll(" C")