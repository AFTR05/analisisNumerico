import matplotlib.pyplot as plt
import numpy as np


def exercicCoeficienteArrastre():
    ##((gravedad(masa)/c)*(1-e^((-c/masa)*10)))-velocidad
    masa = float(input("Ingrese la masa: "))
    velocidad = float(input("Ingrese la velocidad: "))
    x = np.arange(0.1,20,0.0001)
    y = []
    for i in x:
        y.append((((9.8*(masa)/float(i)))*(1-np.exp((-float(i)/masa)*10)))-velocidad)
    plt.plot(x,y)
    plt.plot(x,0*x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funcion coeficiente arrastre')
    plt.grid()
    plt.show()




def exercice_2():
    x = np.arange(3,5,0.0001)
    y = np.sin(10*x)+np.cos(3*x)
    plt.plot(x,y)
    plt.plot(x,0*x,'k-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funcion sin(10x)+cos(3x)')
    plt.grid()
    plt.show()