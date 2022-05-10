# -*- coding: utf-8 -*-

import random as rd

#taille du tableau
n=10

#un tableau de boolean
T=[bool(rd.randint (0 ,1)) for i in range(n)]
print(T)

#on compte le nombre de False
nb_False=0
for i in range(0,n) :
    if T[i]==False:
        nb_False += 1

#on remplit le tableau de False puis de True
for i in range(0,nb_False) :
    T[i] = False
for i in range(nb_False, n):
    T[i] = True

#petite vérification
print(T)

