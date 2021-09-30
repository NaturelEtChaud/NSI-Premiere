from microbit import *

largeur = 1
hauteur = 1

while True:
    if button_a.is_pressed() and largeur != 5:
        largeur = largeur + 2
    if button_b.is_pressed() and hauteur != 5:
        hauteur = hauteur + 2
    for x in range(2-largeur//2,2+largeur//2+1):
        for y in range(2-hauteur//2,2+hauteur//2+1):
            display.set_pixel(x,y,9)
    sleep(200)
    
    if largeur == 5 and hauteur == 5 :
        sleep(2000)
        largeur = 0
        hauteur = 0
        display.clear()
