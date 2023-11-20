import numpy as np
from sympy import *
import matplotlib.pyplot as plt


xi = np.array([ 3, 4,   5,  12,   80,  90],dtype="float64")  
fi = np.array([ 5, 5.5, 6,  6.9,  11,  6.5],dtype="float64")  

n = len(xi)
x = Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)
poli_list = []
poli_listS = []
for i in range(0,n,1):
    
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador
    polisimple = polinomio.expand()
    poli_list.append(polinomio)
    poli_listS.append(polisimple)
    print(i+1, "f(x) = ",polinomio)
    print("--------------------------------'-------------------------------------------")
    print(i+1, "f(x) = ",polisimple)

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = lambdify(x,polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)


# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()

