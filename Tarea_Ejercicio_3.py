import pandas as pd
import matplotlib.pyplot as plt

#Ejercicio 3
#Comparación de Valoraciones
#Calcula y muestra el promedio (media) de tomatometer_rating para todas las películas.
#Crea una nueva columna en tu DataFrame llamada rating_diff que sea la resta entre audience_rating y tomatometer_rating para cada película.
#Genera un histograma de la columna rating_diff. Esto te mostrará visualmente si las diferencias entre audiencia y críticos son mayormente pequeñas,
# grandes, positivas (audiencia califica más alto) o negativas (críticos califican más alto). Nota: Agrupar en intervalos de 30 (bins=30)