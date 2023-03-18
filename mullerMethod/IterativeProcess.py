import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve



def mullerMethod():
    #Function== f(x) = (e^(-x))-x
    graficFunction()
    x0=0 ;  x1=0; x2=1; x3=0.5 ; error=1000 ; i=0
    while(error>0.01):
        x0=x1 ; x1=x2 ; x2=x3
        h0=x1-x0 ; h1=x2-x1 
        s0=(evaluateFunction(x1)-(evaluateFunction(x0)))/(x1-(x0)) ; s1=(evaluateFunction(x2)-(evaluateFunction(x1)))/(x2-(x1))
        a = (s1-(s0))/(h1-(h0))  ; b= a*h1+(s1) ; c = evaluateFunction(x2)
        if(b<0):
            x3 = x2 + (-2*(c))/(b-(math.sqrt((b)**2-4*(a)*(c))))
        elif(b>0): 
            x3 = x2 + (-2*(c))/(b+(math.sqrt((b)**2-4*(a)*(c))))
        print("iteration "+str(i)+" --------------------------------------------------------------------------------------------------")
        print("x3: "+ str(x3))
        if(i!=0):
            error=abs((x3-x2)/x3)*100
            print("Error aproximado: "+str(error))
        i+=1    



def graficFunction():
    x = np.arange(-1,5,0.0001)
    y = f(x)
    plt.plot(x,y)
    plt.plot(x,0*x,'k-')
    raices = fsolve(f, [-2, 5])
    plt.plot(raices, [0]*len(raices), 'ro', label='Raíces')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x) = (e^(-x))-x')
    plt.grid()
    plt.ion()
    plt.draw()
    plt.pause(5)


def f(x):
    return (np.e**(-x))-x

def evaluateFunction(number):
    return ((math.exp(-number))-number)