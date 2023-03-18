import IterativeOperator as io

def metodojacobi():
    io.jacobiMethod()
    
def metodoGaussSeidel():
    io.gaussMethod()


def switch_funcion(option):
    funciones = {
        1: metodojacobi,
        2: metodoGaussSeidel
    }
    funcion = funciones.get(option, lambda: "Opción inválida")
    return funcion()

opcion = int(input("Seleccione una opción:\n 1)Metodo jacobi  2)Metodo Gauss Seidel \n  "))
switch_funcion(opcion)