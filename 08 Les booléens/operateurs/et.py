# -*- coding: utf-8 -*-

def ET(a,b):
    return (a and b)

def tableVerite():
    print('-'*40) #une ligne de  40 symboles -
    tupleBool = (False,True) #un tuple contenant les deux possibilites

    for a in tupleBool:
        for b in tupleBool :
            print(a,"\t et \t",b,"\t = \t",ET(a,b))

    print('-'*40) #une ligne de  40 symboles -
