# -*- coding: utf-8 -*-

def xor(a,b):
    if a:
        return not b
    else :
        return b

def tableVerite():
    print('-'*40) #une ligne de  40 symboles -
    tupleBool = (False,True) #un tuple contenant les deux possibilites
    
    for a in tupleBool:
        for b in tupleBool :
            print(a,"\t ou ex  \t",b,"\t = \t",xor(a,b))
        
    print('-'*40) #une ligne de  40 symboles -
          