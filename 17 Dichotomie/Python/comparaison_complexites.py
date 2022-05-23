# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt     #pour faire le graphique
from math import log

#on trace le graphique avec sa légende
L=[2*i for i in range(1,51)]
L0=[1 for i in range(1,51)] #complexité constante
L1=[2*i for i in range(1,51)] #complexité linéaire
L2=[(2*i)**2 for i in range(1,51)] #complexité quadratique
L3=[log(2*i) for i in range(1,51)] #complexité logarithmique

plt.plot(L,L0,'.',label='complexité constante O(1)')
plt.plot(L,L1,'+',label='complexité linéaire O(n)')
plt.plot(L,L2,'x',label='complexité quadratique O(n²)')
plt.plot(L,L3,'o',label='complexité logarithmique O(log(n))')
plt.legend()
plt.show()

