def f(x):
    ## Representa la funcion que se va a integrar
    return -(0.1*x**2)  +15

def trapecFuntion(y0,y1,h):
    ##Se aplica este metodo cuando  
    #(x+1,x)*(f(x+1)+f(x))/2 +.......n veces
    return (h/2) * (y0 + y1)

def simpson1d3(y0,y1,y2,h):
    ##Se aplica este metodo cuando 3 puntos tienen el mismo espaciado y a fallado el metodo simpson 3/8
    #h*1/3(f(x0)+4*f(x1)+f(x2))
    #h=(x1-x0)
    return (h/3) * (y0 + 4*y1 + y2)

def simpson3d8(y0,y1,y2,y3,h):
    ##se aplica este metodo cuando 4 puntos tiene el mismo espaciado
    #h*3/8(f(x0)+3*f(x1)+3*f(x2)+f(x3))
    #h=(x1-x0)
     
    return (3*h/8) * (y0 + 3*y1 + 3*y2 + y3)



def segmentada_desigual(x):
    n = len(x)-1 # Número de segmentos
    integral = 0
    i=0
    while(i!=n):
        h = x[i+1] - x[i]  # Longitud del segmento                      ## en el metodo de simpson 3/8 h se
                                                                        ##suele tomar en algunas formulas como h=(x3)-(x0)/3
        # Comprobar si se aplica la regla de Simpson 3/8
        if i < n-2 and abs(x[i+3] - x[i+2]) == abs(x[i+2] - x[i+1]) == abs(x[i+1] - x[i]):    ## en el metodo de simpson 3/8 h se
            integral += simpson3d8(f(x[i]),f(x[i+1]),f(x[i+2]),f(x[i+3]),h)
            i += 3  # Saltar dos posiciones debido a la regla de Simpson 3/8
        # Comprobar si se aplica la regla de Simpson 1/3
        elif i < n-1 and abs(x[i+2] - x[i+1]) == abs(x[i+1] - x[i]):
            integral += simpson1d3(f(x[i]),f(x[i+1]),f(x[i+2]),h)
            i += 2 # Saltar una posición debido a la regla de Simpson 1/3
        # Aplicar la regla del trapecio
        else:
            integral += trapecFuntion(f(x[i]),f(x[i+1]),h)
            i+=1
    return integral

# Ejemplo de uso
x=[0,1,3,5,7,9.5,12]

resultado = segmentada_desigual(x)
print("El resultado de la integración es:", resultado)








