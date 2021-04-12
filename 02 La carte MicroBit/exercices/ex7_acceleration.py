from microbit import *

#on crée la liste des 12 images
liste =[Image.CLOCK12,Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,Image.CLOCK9,Image.CLOCK10,Image.CLOCK11]

temps = 500

while True:
    for i in range(12):
        display.show(liste[i])
        sleep(temps)
        if button_a.is_pressed():
            temps += 100
        if button_b.is_pressed() and temps>0:
            temps -= 100