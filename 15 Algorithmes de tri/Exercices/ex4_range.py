# -*- coding: utf-8 -*-

import random as rd

#taille du tableau
n=5

#pour rentrer dans la bouclue
ordre = 0
essais = 0

while(ordre==0) :
    #un tableau de boolean
    T=[rd.randint (0 ,5) for i in range(n)]
    print(T)

    #variable ordre
    #décroissant = -1, rien = 0, croissant = 1
    #on teste T[0] et T[1]
    ordre = -1
    if T[0]<= T[1]:
        ordre = 1

    #on vérifie si l'ordre est respectée
    i=2
    while i<len(T) and ordre !=0 :
        if T[i-1] < T[i] and ordre == -1 :
            ordre = 0
        if T[i-1] > T[i] and ordre == 1 :
            ordre = 0
        i += 1

    print(ordre)
    essais += 1

print(essais,"essais")