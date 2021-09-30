from microbit import *

colonne = 2

while True:
    display.clear()
    for i in range(5):
        display.set_pixel(colonne, i, 9)
    if button_a.is_pressed():
        colonne = colonne - 1
    if button_b.is_pressed():
        colonne = colonne + 1
    if colonne == -1:
        colonne = 4
    if colonne == 5:
        colonne = 0
    sleep(100)
