import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
import math

df = pd.read_csv("death.csv")
# Calcular la correlación de Pearson
correlacion = df['edad'].corr(df['tamaño_del_tumor'])

# Imprimir el resultado
print("Correlación de Pearson:", correlacion)
# Calcular la correlación de Pearson
X = df[['edad']]
y = df['tamaño_del_tumor']

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
modelo.fit(X, y)

# Realizar predicciones
predicciones = modelo.predict(X)

# Imprimir los coeficientes de la regresión
print("Coeficiente (pendiente):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Graficar los datos y la línea de regresión
plt.scatter(X, y, color='blue', label='Datos')
plt.plot(X, predicciones, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Edad')
plt.ylabel('Tamaño del Tumor')
plt.legend()
plt.show()