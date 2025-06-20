# Importar pandas para manejo de datos
import pandas as pd

# Cargar el archivo Excel original con los datos del mercado
df = pd.read_excel("Mercado2_casa.xlsx")

# Crear una copia del DataFrame para mantener el original intacto
df_limpio = df.copy()

# Identificar las columnas que son numéricas (para aplicar la eliminación de outliers)
columnas_numericas = df.select_dtypes(include='number').columns

# Recorrer cada columna numérica para aplicar la regla del IQR
for columna in columnas_numericas:
    # Calcular el primer cuartil (Q1) y el tercer cuartil (Q3)
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)

    # Calcular el rango intercuartílico (IQR)
    iqr = q3 - q1

    # Establecer límites inferior y superior
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    # Filtrar la tabla para mantener solo los datos dentro del rango permitido
    df_limpio = df_limpio[
        (df_limpio[columna] >= limite_inferior) &
        (df_limpio[columna] <= limite_superior)
    ]

# Mostrar el DataFrame limpio (sin outliers)
print("Datos sin outliers (todas las columnas):")
print(df_limpio)
