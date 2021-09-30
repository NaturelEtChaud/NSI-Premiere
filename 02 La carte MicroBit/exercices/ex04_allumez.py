from microbit import *

largeur_ligne = 0
largeur_colonne = 0

while True:
    if button_a.is_pressed() and largeur_colonne<2:
        largeur_colonne += 1
    if button_b.is_pressed() and largeur_ligne<2:
        largeur_ligne += 1

    for i in range(2-largeur_colonne, 2+largeur_colonne+1):
            for j in range(2-largeur_ligne, 2+largeur_ligne+1):
                display.set_pixel(i, j, 9)
    sleep(100)

    if largeur_colonne == 2 and largeur_ligne == 2:
        sleep(1900)
        # réinitialisation
        largeur_ligne = 0
        largeur_colonne = 0
        display.clear()
