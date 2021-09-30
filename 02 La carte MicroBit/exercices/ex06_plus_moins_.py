from microbit import *

def wait():
    sleep(1800)
    display.clear()
    sleep(200)

while True:
    #le signe +
    for i in range(5):
        display.set_pixel(i,2,9)
        display.set_pixel(2,i,9)

    wait()

    #le signe -
    for i in range(5):
        display.set_pixel(i,2,9)

    wait()

    #le signe x
    for i in range(5):
        display.set_pixel(i,i,9)
        display.set_pixel(4-i,i,9)

    wait()

    #le signe /
    for i in range(5):
        display.set_pixel(4-i,i,9)

    wait()
