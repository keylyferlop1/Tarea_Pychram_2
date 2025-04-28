import pandas as pd
import matplotlib.pyplot as plt

#Ejercicio 5
#Cuenta cuántas películas ha dirigido cada director usando value_counts() en la columna directors.
#Muestra los 10 directores que aparecen con más frecuencia.
#Calcula el promedio de tomatometer_rating para las películas de solo estos 10 directores.
# Pista: Puedes filtrar el DataFrame original para incluir solo las filas de estos directores y
# luego usar groupby('directors')['tomatometer_rating'].mean().


