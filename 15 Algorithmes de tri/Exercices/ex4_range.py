# -*- coding: utf-8 -*-

import random as rd


def croissant(tab,i):
    """
    les premières cases sont dans l'ordre croissant
    on vérifie pour la suite
    """
    ordre = True
    while ordre and (i<len(tab)) :
        if tab[i] < tab[i-1]:
            ordre = False
        i = i + 1
    return ordre

def decroissant(tab,i):
    """
    les deux premières cases sont dans l'ordre decroissant
    on vérifie pour la suite
    """
    ordre = True
    while ordre and (i<len(tab)) :
        if tab[i] > tab[i-1]:
            ordre = False
        i = i + 1
    return ordre

def est_trier(tab):
    """
    On regarde uniquement les premières cases
    On renvoie :
    0 si le tableau n'est pas trié
    1 si le tableau est trié dans l'odre croissant
    2 si le tableau est trié dans l'ordre décroissant
    3 si le tableau est constant
    """
    i = 1
    while i<len(tab) and tab[i] == tab[i-1] :
        i = i + 1
    if i == len(tab):
        return 3
    elif tab[i] > tab[i-1] :
        if croissant(tab,i) :
            return 1
        else :
            return 0
    else :
        if decroissant(tab,i) :
            return 2
        else :
            return 0


####
# pour vérification
####
if __name__ == "__main__":
    #   taille du tableau
    n=10
    T=[rd.randint (0 ,10) for i in range(n)]
    print(T)
    print(est_trier(T))
    T_croi = [0,0,0,0,1,2,3,5]
    print(est_trier(T_croi))
    T_dec = [6,6,6,3,2,0,0,0,0]
    print(est_trier(T_dec))
    T_cst = [8,8,8,8,8,8,8]
    print(est_trier(T_cst))


