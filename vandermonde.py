# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:48:31 2023

@author: MARIO
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([ 3, 4,   5,  12,   80,  90],dtype="float64")  
y = np.array([ 5, 5.5, 6,  6.9,  11,  6.5],dtype="float64")  

V = np.vander(x, increasing=True)

coeficientes = np.linalg.solve(V, y)
print("Los coeficientes: ", coeficientes[::-1])

P=np.poly1d(coeficientes[::-1])	

print("La temperatura a las 4am es ", P(4), " y ", "a las 8am es ", P(8))
xpi=[4,8]
ypi=[P(4),P(8)]



print("El polinomio: ")
print(P)


xp = np.linspace(min(x), max(x), 100)
yp = P(xp)

plt.plot(xp, yp, label='Polinomio Interpolante', linestyle='--')
plt.scatter(x, y, label='Puntos de Interpolacion', color='red', marker='o')
# plt.scatter(xpi, ypi, label='Puntos deseados', color='green', marker='v')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(ls="dashed")
plt.legend()

