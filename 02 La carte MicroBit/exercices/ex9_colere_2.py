from microbit import *

#on prend une mesure au repos pour référence
repos = accelerometer.get_z()

while True:
    display.show(Image.ASLEEP)
    etat=accelerometer.get_z()
    print(etat)
    if abs(etat-repos)>200:
        display.show(Image.ANGRY)
        sleep(5000)
