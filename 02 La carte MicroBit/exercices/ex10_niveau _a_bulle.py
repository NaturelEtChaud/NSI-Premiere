from microbit import *

x , y = 2, 2

while not button_a.is_pressed() :
    x = x + accelerometer.get_x() / 1000
    y = y + accelerometer.get_y() / 1000
    if(x>4): x = 4
    if(x<0): x = 0
    if(y>4): y = 4
    if(y<0): y = 0
    sleep(100)
    display.clear()
    display.set_pixel(int(x),int(y),9)