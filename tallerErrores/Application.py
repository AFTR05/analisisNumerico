import Error

def optionExp():
    Error.exp()

def optionCos():
    Error.cos()
    
def optionSin():
    Error.sin()

def optionCosValor():
    Error.cosConValorReal()   

def switch_funcion(option):
    funciones = {
        1: optionExp,
        2: optionCos,
        3: optionSin,
        4: optionCosValor
    }
    funcion = funciones.get(option, lambda: "Opción inválida")
    return funcion()

opcion = int(input("Seleccione una opción 1) Exponencial 2) Coseno 3) Sen 4) Coseno con valor real:  "))
switch_funcion(opcion)