import pandas as pd
import matplotlib.pyplot as plt

#Ejercicio 1
#1. Carga del Dataset
#la fecha de estreno esté en el formato correcto (datetime).
# Importa las librerías necesarias: pandas para manejo de datos y matplotlib.pyplot para gráficos.
# Lee el archivo “Rotten Tomatoes Movies.csv” en un DataFrame de pandas. Llama a tu DataFrame df_movies.
# Muestra las primeras 5 filas del DataFrame (df_movies.head()) para ver cómo se ven los datos.
# Verifica los tipos de datos de cada columna (df_movies.info() o df_movies.dtypes).
# Fíjate en el tipo de dato de in_theaters_date.
# Convierte la columna in_theaters_date al tipo de dato datetime. Esto nos permite tratar las fechas como fechas reales y
# no solo texto. Usa pd.to_datetime(). Pista: Si encuentras errores, puedes añadir errors='coerce' dentro de pd.to_datetime()
# para convertir fechas inválidas en NaT (Not a Time).
# Verifica nuevamente los tipos de datos (df_movies.dtypes) para confirmar que in_theaters_date ahora es de tipo datetime64[ns].
df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# Carga del Dataset
print(df_movies.dtypes)

# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
print("\nPrimeras 5 filas del DataFrame:")
print(df_movies.head())

# 4. Verificar los nombres de las columnas
print("\nNombres de las columnas:")
print(df_movies.columns)

# 5. Convertir la columna 'in_theaters_date' al tipo datetime
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 6. Verificar que la conversión fue exitosa (dtypes)
print("\nTipos de datos después de la conversión:")
print(df_movies.dtypes)

# 7. Mostrar si hubo valores no convertidos (NaT)
missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")

