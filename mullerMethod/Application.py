import IterativeProcess as ip

def mullerMethod():
    ip.mullerMethod()
    



def switch_funcion(option):
    funciones = {
        1: mullerMethod
    }
    funcion = funciones.get(option, lambda: "Opción inválida")
    return funcion()

opcion = int(input("Seleccione una opción:\n 1)Metodo Muller \n  "))
switch_funcion(opcion)