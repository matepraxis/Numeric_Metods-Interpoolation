# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:09:12 2023

@author: MARIO
"""

import numpy as np
import matplotlib.pyplot as plt

import numpy.polynomial.polynomial as pol


x = np.array([ 3, 4,   5,  12,   80,  90],dtype="float64")  
y = np.array([ 5, 5.5, 6,  6.9,  11,  6.5],dtype="float64")  



xp = np.linspace(min(x),max(x))
p  = pol.polyfit(x,y,len(x)-1)

p2=np.poly1d(p[::-1])
print(p2)

yp = pol.polyval(xp,p)


print(p)

plt.figure()
plt.plot(xp,yp,'b-', label = 'polinomio interpolante')
plt.plot( x, y,'ro', label = 'puntos')
plt.legend()
plt.show()