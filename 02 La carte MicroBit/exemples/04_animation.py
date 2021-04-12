from microbit import *

#on crée la liste des 12 images
liste =[Image.CLOCK12,Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,Image.CLOCK9,Image.CLOCK10,Image.CLOCK11]

while True:
    for i in range(12):
        display.show(liste[i])
        sleep(500)
