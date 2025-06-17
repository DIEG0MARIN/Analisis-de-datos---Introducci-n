#Paso 1: Leer el archivo CSV
import pandas as pd
import numpy as np
#pip install pandas numpy

df = pd.read_csv('diabetes_ejemplo.csv') #utiliza la función read_csv de la librería pandas (importada como pd) para leer un archivo CSV llamado diabetes_ejemplo.csv y cargar su contenido en un DataFrame llamado df, que es una estructura de datos en forma de tabla con filas y columnas, similar a una hoja de Excel, donde cada columna puede contener distintos tipos de datos.
print(df)

#Paso 2: Hacer un muestreo aleatorio simple
#Opción A. Seleccionar n registros aleatorios
muestra = df.sample(n=5, random_state=42)  # Cambia n si quieres más o menos registros. selecciona de forma aleatoria 5 filas del DataFrame df y las guarda en la variable muestra; el parámetro random_state=42 se usa para que el resultado del muestreo sea siempre el mismo cada vez que se ejecute el código, lo cual es útil para asegurar la reproducibilidad del análisis.
print("\nMuestra aleatoria de 5 registros:") 
print(muestra)

#Opción B Seleccionar un porcentaje (fracción) del total
muestra_porcentaje = df.sample(frac=0.3, random_state=42)  # 30% del total
print("\nMuestra aleatoria del 30%:")
print(muestra_porcentaje)





