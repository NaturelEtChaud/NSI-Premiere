# -*- coding: utf-8 -*-

def negation(a):
    return not a

def tableVerite():
    print('-'*30) #une ligne de  30 symboles -
    tupleBool = (False,True) #un tuple contenant les deux possibilites

    for a in tupleBool:
        print("La negation de",a,"est",negation(a))

    print('-'*30) #une ligne de  30 symboles -
