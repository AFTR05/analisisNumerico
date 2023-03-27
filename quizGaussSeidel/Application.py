import QuizOperator as io


    
def quizGaussSeidel():
    io.gaussMethod()

def switch_funcion(option):
    funciones = {
        1: quizGaussSeidel
    }
    funcion = funciones.get(option, lambda: "Opción inválida")
    return funcion()

opcion = int(input("Seleccione una opción:\n 1)Metodo Gauss Seidel \n  "))
switch_funcion(opcion)