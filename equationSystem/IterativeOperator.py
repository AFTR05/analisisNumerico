def jacobiMethod():
    lastx1=round((0.4+(0)+(0))/2,5)
    lastx2=round((4.7-3*(0)-2*(0))/5,5)
    lastx3=round((7.9-(0)-3*(0))/4,5)
    nowx1=lastx1
    nowx2=lastx2
    nowx3=lastx3
    x1error=1000
    x2error=1000
    x3error=1000
    counter=1
    print("Iteracion "+ str(counter) +" -------------------------------------------------------------------------------------------")
    print('El valor de x1 es: '+str(lastx1))
    print('El valor de x2 es: '+str(lastx2))
    print('el valor de x3 es: '+str(lastx3))
    counter+=1
    while(x1error>=0.04 or x2error>=0.04 or x3error>=0.04):
        lastx1=nowx1
        lastx2=nowx2
        lastx3=nowx3
        nowx1=round((0.4+(lastx2)+(lastx3))/2,5)
        nowx2=round((4.7-3*(lastx1)-2*(lastx3))/5,5)
        nowx3=round((7.9-(lastx1)-3*(lastx2))/4,5)
        x1error=abs(((nowx1-(lastx1))/nowx1)*100)   
        x2error=abs(((nowx2-(lastx2))/nowx2)*100)
        x3error=abs(((nowx3-(lastx3))/nowx3)*100)
        print("Iteracion "+ str(counter) +" -------------------------------------------------------------------------------------------")
        print('El valor de x1 es: '+str(nowx1))
        print('El error porcentual de x1 es: '+str(x1error))
        print('El valor de x2 es: '+str(nowx2))
        print('El error porcentual de x2 es: '+str(x2error))
        print('el valor de x3 es: '+str(nowx3))
        print('El error porcentual de x3 es: '+str(x3error))
        counter+=1
    print("Iteracion "+ str(counter) +" -------------------------------------------------------------------------------------------")
    print('El valor de x1 es: '+str(nowx1))
    print('El error porcentual de x1 es: '+str(x1error))
    print('El valor de x2 es: '+str(nowx2))
    print('El error porcentual de x2 es: '+str(x2error))
    print('el valor de x3 es: '+str(nowx3))
    print('El error porcentual de x3 es: '+str(x3error))    
    print('fin de programa')
        
def gaussMethod():
    lastx1=round((0.4+(0)+(0))/2,5)
    lastx2=round((4.7-3*(lastx1)-2*(0))/5,5)
    lastx3=round((7.9-(lastx1)-3*(lastx2))/4,5)
    nowx1=lastx1
    nowx2=lastx2
    nowx3=lastx3
    x1error=1000
    x2error=1000
    x3error=1000
    counter=1
    print("Iteracion "+ str(counter) +" -------------------------------------------------------------------------------------------")
    print('El valor de x1 es: '+str(lastx1))
    print('El valor de x2 es: '+str(lastx2))
    print('el valor de x3 es: '+str(lastx3))
    counter+=1
    while(x1error>=0.04 or x2error>=0.04 or x3error>=0.04):
        lastx1=nowx1
        lastx2=nowx2
        lastx3=nowx3
        nowx1=round((0.4+(nowx2)+(nowx3))/2,5)
        nowx2=round((4.7-3*(nowx1)-2*(nowx3))/5,5)
        nowx3=round((7.9-(nowx1)-3*(nowx2))/4,5)
        x1error=abs(((nowx1-(lastx1))/nowx1)*100)   
        x2error=abs(((nowx2-(lastx2))/nowx2)*100)
        x3error=abs(((nowx3-(lastx3))/nowx3)*100)
        print("Iteracion "+ str(counter) +" -------------------------------------------------------------------------------------------")
        print('El valor de x1 es: '+str(nowx1))
        print('El error porcentual de x1 es: '+str(x1error))
        print('El valor de x2 es: '+str(nowx2))
        print('El error porcentual de x2 es: '+str(x2error))
        print('el valor de x3 es: '+str(nowx3))
        print('El error porcentual de x3 es: '+str(x3error))
        counter+=1
    print("Iteracion "+ str(counter) +" -------------------------------------------------------------------------------------------")
    print('El valor de x1 es: '+str(nowx1))
    print('El error porcentual de x1 es: '+str(x1error))
    print('El valor de x2 es: '+str(nowx2))
    print('El error porcentual de x2 es: '+str(x2error))
    print('el valor de x3 es: '+str(nowx3))
    print('El error porcentual de x3 es: '+str(x3error))    
    print('fin de programa')