import math


def exp():
    n=1
    inputValor=input('Ingrese el valor a evaluar la funcion exp: ')
    cifraSigni=input('Escriba el valor de las cifras significativas: ')
    valorActual=(float(inputValor)**0/math.factorial(0))
    print('el valor de la exp: ',valorActual)
    valorViejo=(float(inputValor)**0/math.factorial(0))
    errorAproxNormal=100
    print('el error aproximado normalizado:',errorAproxNormal)
    while(errorAproxNormal>float(0.5*10**(2-int(cifraSigni)))):
        valorActual+=(float(inputValor)**n/math.factorial(n))
        print('Suscesion ',n,'---------------------------------------------------------------------')
        n=n+1
        errorAproxNormal=((valorActual-valorViejo)/valorViejo)*100
        print('El error verdadero es: ',str(valorActual-valorViejo))
        print('El error absoluto es: ',str(abs(valorActual-valorViejo)))
        print('el error aproximado normalizado es: ',errorAproxNormal,'%')
        print('el valor actual es: ',valorActual)
        valorViejo=valorActual
    


def cos():
    n=1 #contador de las series
    inputValor=input('Ingrese el valor a evaluar la funcion cos (si su valor es π digite y): ') #valor para evaluar laa serie
    if(inputValor=='y'):
        inputValor=math.pi*float(input('Ingrese el valor a multiplicar π: ')) #peticion de valor de pi 
    else:
        inputValor=input('Ingrese el valor a evaluar la funcion cos: ') 
    cifraSigni=input('Escriba el valor de las cifras significativas: ') #peticion de valor de las cifras significativas
    valorActual=(((-1)**0)/math.factorial(2*0))*(float(inputValor)**(2*0)) #operacion de la serie con valor incial
    print('el valor de la cos: ',valorActual)
    valorViejo=(((-1)**0)/math.factorial(2*0))*(float(inputValor)**(2*0))  #se iguala con el valor actual
    errorAproxNormal=100 
    print('el error aproximado normalizado:',errorAproxNormal,'%')
    while(abs(errorAproxNormal)>float(0.5*10**(2-int(cifraSigni)))):  #condicion para ver si el error es mayor a Es
        valorActual+=(((-1)**n)/math.factorial(2*n))*(float(inputValor)**(2*n))
        print('Suscesion ',n,'---------------------------------------------------------------------')
        n=n+1
        errorAproxNormal=(((valorActual-valorViejo)/valorViejo)*100)  # operacion de error aproximado normalizado
        print('El error verdadero es: ',str(valorActual-valorViejo)) 
        print('El error absoluto es: ',str(abs(valorActual-valorViejo)))
        print('el error aproximado normalizado es: ',errorAproxNormal,'%')   #se imprime
        print('el valor actual es: ',valorActual)
        valorViejo=valorActual
    print('El error verdadero es: ',str(valorActual-valorViejo))
    print('El error absoluto es: ',str(abs(valorActual-valorViejo)))    # se imprime
    print('el error aproximado normalizado es: ',errorAproxNormal,'%')
    print('el valor actual es: ',valorActual)


def sin():
    n=1
    inputValor=input('Ingrese el valor a evaluar la funcion sin (si su valor es π digite y): ')
    if(inputValor=='y'):
        inputValor=math.pi*float(input('Ingrese el valor a multiplicar π: '))
    else:
        inputValor=input('Ingrese el valor a evaluar la funcion cos: ')
    cifraSigni=input('Escriba el valor de las cifras significativas: ')
    valorActual=(((-1)**0)/math.factorial(2*0+1))*(float(inputValor)**(2*0+1))
    print('el valor de la sin: ',valorActual)
    valorViejo=(((-1)**0)/math.factorial(2*0+1))*(float(inputValor)**(2*0+1))
    errorAproxNormal=100
    print('el error aproximado normalizado:',errorAproxNormal,'%')
    while(errorAproxNormal>float(0.5*10**(2-int(cifraSigni)))):
        valorActual+=(((-1)**n)/math.factorial(2*n+1))*(float(inputValor)**(2*n+1))
        print('Suscesion ',n,'---------------------------------------------------------------------')
        n=n+1
        errorAproxNormal=abs(((valorActual-(valorViejo))/valorViejo)*100)
        print('El error verdadero es: ',str(valorActual-(valorViejo)))
        print('El error absoluto es: ',str(abs(valorActual-(valorViejo))))
        print('el error aproximado normalizado es: ',errorAproxNormal,'%')
        print('el valor actual es: ',valorActual)
        valorViejo=valorActual
    
        



def cosConValorReal():
    n=1
    inputValor=input('Ingrese el valor a evaluar la funcion cos (si su valor es π digite y): ')   #valor para evaluar laa serie

    if(inputValor=='y'):
        inputValor=math.pi*float(input('Ingrese el valor a multiplicar π: '))    #peticion de valor de pi

        if(input('desea ingresar valor a divisor (y/n)')=='y'):
            inputValor=inputValor/float(input('Ingrese el valor a dividir: '))        
    else:
        inputValor=input('Ingrese el valor a evaluar la funcion cos: ') 
    cifraSigni=input('Escriba el valor de las cifras significativas: ')    #peticion de valor de las cifras significativas

    valorActual=(((-1)**0)/math.factorial(2*0))*(float(inputValor)**(2*0))          # se inicia la serie con valor incial

    valorViejo=math.cos(float(inputValor))                                     #se hace el valor real
    print('el valor de la cos: ',valorViejo)
    print('el valor de la cos con valor real: ',valorViejo)
    errorAproxNormal=100
    print('el error aproximado normalizado:',errorAproxNormal,'%')
    while(errorAproxNormal>float(0.5*10**(2-int(cifraSigni)))):             #condicion para ver si el error es mayor a Es
        valorActual+=(((-1)**n)/math.factorial(2*n))*(float(inputValor)**(2*n))   # sumatoria de la serie

        print('Suscesion ',n,'---------------------------------------------------------------------')
        n=n+1
        errorAproxNormal=abs(((valorActual-(valorViejo))/valorViejo)*100)    # operacion de error aproximado normalizado

        print('El error verdadero es: ',str(valorActual-(valorViejo)))
        print('El error absoluto es: ',str(abs(valorActual-(valorViejo))))    # se imprime

        print('el error aproximado normalizado es: ',errorAproxNormal,'%')
        print('el valor actual es: ',valorActual)


    









