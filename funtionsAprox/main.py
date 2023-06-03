import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
#Puntos
#(0,98)
#(5,55)
#(10,35.5)
#(15,20)
#(25,8)
# Ejemplo de uso
x_values = [0,5,15,25,30]
y_values = [98,55,20,8,5.5]
Pv=np.vander(x_values,len(x_values))
print(Pv)
Xs=np.linalg.solve(Pv,y_values)
print(Xs)
P=np.poly1d(Xs)
print(P)
x1=np.linspace(min(x_values),max(x_values),num=100)
y1=P(x1)
plt.plot(x_values, y_values, 'o', label='Datos originales')
plt.plot(x1,y1,"-",label='Polinomio Interpolado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
