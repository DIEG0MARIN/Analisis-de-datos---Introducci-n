# En la terminal instalar pandas: pip install pandas

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('alturas_plantas.csv')

# Ver los datos (opcional)
print(df)

# Calcular la media aritmética de la columna 'Altura'
media = df['Altura'].mean()

# Calcular la mediana de la columna 'Altura'
mediana = df['Altura'].median()

# Calcular la moda de la columna 'Altura'
moda = df['Altura'].mode()

# Mostrar el resultado
print(f"La media aritmética de las alturas es: {media}")
print(f"La mediana de las alturas es: {mediana}")
print(f"La moda de las alturas es: {moda}")
print(moda.tolist())