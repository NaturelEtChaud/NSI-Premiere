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
                if i==2 and j==2:
                    intensite = 9
                elif abs(2-i)==2 or abs(2-j)==2:
                    # un écart de 2 par rapport au centre
                    intensite = 3
                else :
                    # un écart de 1 par rapport au centre
                    intensite = 6
                display.set_pixel(i, j, intensite)
    sleep(100)

    if largeur_colonne == 2 and largeur_ligne == 2:
        sleep(1900)
        # réinitialisation
        largeur_ligne = 0
        largeur_colonne = 0
        display.clear()
