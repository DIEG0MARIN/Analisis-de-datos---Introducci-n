# Muestreo de elementos por columnas con NumPy

import pandas as pd
import numpy as np

# Leer el archivo CSV
df = pd.read_csv('diabetes_ejemplo.csv')

# Muestreo aleatorio de 10 valores de la columna 'glucosa'
# df_muestra = np.random.choice(df["glucosa"], 10)

# Muestreo sin repeticiones
df_muestra = np.random.choice(df["glucosa"], 10, replace=False)


# Imprimir los resultados
print("\nMuestreo de elementos por columna (10 elementos)")
print(df_muestra)



