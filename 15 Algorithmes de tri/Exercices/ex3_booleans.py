# -*- coding: utf-8 -*-

import random as rd


def tri_bool(tab):
    # on compte le nombre de nb de False
    nb_false = 0
    for i in range(len(tab)):
        if tab[i]==False:
            nb_false = nb_false + 1
    # on reconstruit le tableau
    for i in range(0,nb_false):
        tab[i] = False
    for i in range(nb_false,n):
        tab[i] = True
    return tab

# une variante avec la reconstruction par compréhension
def tri_bool_v2(tab):
    # on compte le nombre de nb de False
    nb_false = 0
    for i in range(len(tab)):
        if tab[i]==False:
            nb_false = nb_false + 1
    # on reconstruit le tableau
    tab = [i>=nb_false for i in range(n)]
    return tab


####
# pour vérification
####
if __name__ == "__main__":
    #   taille du tableau
    n=10
    # un tableau de boolean
    T=[bool(rd.randint (0 ,1)) for i in range(n)]
    print(T)
    #T = tri_bool(T)
    #print(T)
    T = tri_bool_v2(T)
    print(T)
