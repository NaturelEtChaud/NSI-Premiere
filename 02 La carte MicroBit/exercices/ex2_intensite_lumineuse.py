from microbit import *

intensite = 9

while True:
    display.set_pixel(2, 2, intensite)
    if button_a.is_pressed() and intensite >0:
        intensite -= 1
    if button_b.is_pressed() and intensite <9:
        intensite += 1
    sleep(100)