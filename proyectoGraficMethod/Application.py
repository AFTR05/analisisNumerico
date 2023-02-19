import matplotlib.pyplot as plt
import Graficator as grf
import numpy as np

def optionArrastre():
    grf.exercicCoeficienteArrastre()

def optionExercise2():
    grf.exercice_2()


def switch_funcion(option):
    funciones = {
        1: optionArrastre,
        2: optionExercise2
    }
    funcion = funciones.get(option, lambda: "Opción inválida")
    return funcion()

opcion = int(input("Seleccione una opción:\n 1)Coeficiente de arrastre   2)Exercise 2 \n  "))
switch_funcion(opcion)

