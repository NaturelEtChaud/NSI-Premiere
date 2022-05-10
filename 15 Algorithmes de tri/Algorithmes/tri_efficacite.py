# -*- coding: utf-8 -*-

import random as rd                 #pour le hasard
from time import perf_counter       #pour l'horloge compteur
import matplotlib.pyplot as plt     #pour faire le graphique

########################
#fonction tri insertion
#######################
def tri_insertion(T):
    for i in range(1,len(T)) :
        j = i
        while (j > 0) and (T[j-1] > T[j]) :
            T[j], T[j-1] = T[j-1], T[j]
            j = j - 1

########################
#fonction tri sélection
#######################
def tri_selection(T):
    for i in range(0,len(T)) :
        indice_min = i
        for j in range(i+1,len(T)) :
            if T[indice_min] > T[j] :
                indice_min = j
        T[indice_min], T[i] = T[i], T[indice_min]

########################
#fonction tri sort de Python
#######################
def tri_sort(T):
    #tout est bien caché
    T.sort()

########################
#fonction compteur
#######################
def test(N,tri):
    L=[rd.randint(0,100) for i in range(N)]
    t0=perf_counter()
    tri(L)
    return perf_counter()-t0

########################
#création du graphique
#######################
#trois listes de séries de 50 tests avec 100 valeurs de plus à chaque fois.
L1,L2,L3=[],[],[]
for i in range(1,51):
    L1.append(test(100*i,tri_insertion))
    L2.append(test(100*i,tri_selection))
    L3.append(test(100*i,tri_sort))

#on trace le graphique avec sa légende
L=[100*i for i in range(1,51)]
plt.plot(L,L1,'+',label='insertion')
plt.plot(L,L2,'x',label='selection')
plt.plot(L,L3,':',label='tri sort()')
plt.legend()
plt.show()