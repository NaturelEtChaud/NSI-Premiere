# -*- coding: utf-8 -*-

import random as rd                 #pour le hasard
from time import perf_counter       #pour l'horloge compteur
import matplotlib.pyplot as plt     #pour faire le graphique

########################
#fonction recherche naive
#######################
def naive(T,v):
    indice = -1
    i = 0
    while i<len(T) and indice==-1 :
        if T[i] == v :
            indice = i
        i = i + 1
    return indice


########################
#fonction recherche dichotomique
#######################
def dicho(T,v):
    n = len(T)
    
    mini = 0
    med = 0
    maxi = n-1
    while mini < maxi:
        med = (mini + maxi)//2
        if T[med]< v :
            #v est dans la partie supérieure du tableau
            mini = med +1
        elif T[med] > v :
            #v est dans la partie inférieure du tableau
            maxi = med -1
        else :
            maxi = med
            mini = med
    if T[mini]==v :
        indice = mini
    else:
        indice = -1

    return indice


########################
#fonction compteur
#######################
def test(n,recherche):
    #création d'un tableau croissant de n cases
    T=[0]*n
    for i in range(n):
        T[i] = T[i-1]+rd.randint(0,10)
    #création de la valeur à rechercher
    v = rd.randint(0,10*n)
    #on compte le temps
    t0=perf_counter()
    recherche(T,v)
    return perf_counter()-t0


########################
#création du graphique
#######################
#50 tests avec des tableaux le longueurs 100 000 à 500 0000
L1,L2=[],[]
for i in range(1,51):
    print(i) #affichage du compteur pour patienter
    L1.append(test(100000*i,naive))
    L2.append(test(100000*i,dicho))

#on trace le graphique avec sa légende
L=[100000*i for i in range(1,51)]
plt.plot(L,L1,'+',label='algorithme de recherche naïf')
plt.plot(L,L2,'x',label='algorithme de recherche dichotomique')
plt.legend()
plt.show()