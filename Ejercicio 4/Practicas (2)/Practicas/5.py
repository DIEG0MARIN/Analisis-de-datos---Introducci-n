# Importar pandas
import pandas as pd

# Cargar el archivo Excel con los datos originales
df_original = pd.read_excel("LimpiezaOrtografia.xlsx", sheet_name="Datos")

# Hacer una copia del DataFrame original
df = df_original.copy()

# Convertir la columna 'Nombre' a mayúsculas
df["Nombre"] = df["Nombre"].str.upper()

# Convertir la columna 'Ciudad' a mayúsculas
df["Ciudad"] = df["Ciudad"].str.upper()

# Mostrar mensaje y resultado
print("Convertir a Mayúsculas")
print(df)
