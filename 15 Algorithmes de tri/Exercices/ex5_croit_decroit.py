# -*- coding: utf-8 -*-

import random as rd

#taille du tableau
n=10

##########################################
#création d'un tableau dans l'ordre décroissant
##########################################
#un tableau de taille n rempli de zéros
T=[0]*n
T[0] = rd.randint(0,10000)
for i in range (1,n):
    T[i] = rd.randint(0,T[i-1])
#vérification
print(T)

###########################################
#rangement du tableau dans l'ordre croissant
###########################################
#on prend un tableau intermédiaire de même taille
Temp =[0]*n

#les derniers seront les premiers
for i in range(n):
    Temp[i] = T[n-1-i]

#on remet les valeurs de Temp dans T dans le même ordre
for i in range(n):
    T[i] = Temp[i]

#vérification
print(T)