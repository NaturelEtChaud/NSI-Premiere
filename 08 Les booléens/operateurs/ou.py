# -*- coding: utf-8 -*-

def OU(a,b):
    return (a or b)

def tableVerite():
    print('-'*40) #une ligne de  40 symboles -
    tupleBool = (False,True) #un tuple contenant les deux possibilites

    for a in tupleBool:
        for b in tupleBool :
            print(a,"\t ou \t",b,"\t = \t",OU(a,b))

    print('-'*40) #une ligne de  40 symboles -
