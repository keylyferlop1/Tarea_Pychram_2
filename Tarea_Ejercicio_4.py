import pandas as pd
import matplotlib.pyplot as plt

#Ejercico 4
# Análisis por Género
#Este paso se requiere manejar géneros múltiples. Primero, crea una copia de tu DataFrame para no modificar el original.
#En la copia, divide la columna genre por “,” para obtener una lista de géneros para cada película y expande estas listas para que cada género tenga su propia fila.
#Pista: Usa .str.split(',').explode(). Asigna el resultado generado en un nuevo DataFrame “df_genres_exploded”.
#Usando df_genres_exploded, calcula el promedio de audience_rating para cada género individual. Pista: Usa groupby('genre')['audience_rating'].mean().
#Muestra los 10 géneros con el promedio de calificación de audiencia más alto haciendo uso de un diagrama de pastel. 