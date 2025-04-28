import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# Carga del Dataset
print(df_movies.dtypes)

#Ejercicio 2
#Se realizará una exploración inicial del dataset para conocer su tamaño,los géneros más comunes y las categorías de calificación.

#1 ¿Cuántas películas hay? Muestra el número total de filas en el DataFrame (que corresponde al número de películas). Pista: Usa len() o df_movies.shape.

#2 ¿Cómo se distribuyen las calificaciones? Cuenta cuántas películas pertenecen a cada categoría en tomatometer_status (Certified Fresh, Fresh, Rotten) usando value_counts().

#3 Visualiza la distribución de calificaciones: Crea un gráfico circular (pie chart) simple para mostrar la proporción de cada tomatometer_status. Asegúrate de añadir etiquetas.

# Número total de películas
total_peliculas = len(df_movies)
print(f"Número total de películas: {total_peliculas}")

# 8. Número total de películas
total_peliculas = len(df_movies)
print(f"\n8. Número total de películas en el dataset: {total_peliculas}")

# 10. Distribución de películas por tomatometer_status
distribucion_calificaciones = df_movies['tomatometer_status'].value_counts()
print("\n10. Distribución de películas por tomatometer_status:")
print(distribucion_calificaciones)

# Crear gráfico circular
plt.figure(figsize=(6, 6))
distribucion_calificaciones.plot.pie(
    autopct='%1.1f%%',     # Muestra el porcentaje con 1 decimal
    startangle=90,         # Empieza desde arriba
    labels=distribucion_calificaciones.index,  # Etiquetas de cada sección
    shadow=True            # Sombra para darle profundidad
)

plt.title('Distribución de Calificaciones (Tomatometer Status)')
plt.ylabel('')  # Oculta la etiqueta del eje Y
plt.show()