# importar la libreria pandas
import pandas as pd

# Cargar el archivo Excel con los datos del mercado
df = pd.read_excel("Mercado2_casa.xlsx")

# Calcular los cuartiles de la columna 'Carnes'
q1 = df["Carnes"].quantile(0.25)  # Cuartil 1 (25% de los datos)
q2 = df["Carnes"].quantile(0.50)  # Cuartil 2, también llamado Mediana
q3 = df["Carnes"].quantile(0.75)  # Cuartil 3 (75% de los datos)

# Calcular el IQR (Rango Intercuartílico), es decir, la dispersión central de los datos
iqr = q3 - q1

# Establecer los límites inferior y superior para detectar valores atípicos (outliers)
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Filtrar los datos para quedarnos solo con los que están dentro del rango válido
df_sin_outliers = df[(df["Carnes"] >= limite_inferior) & (df["Carnes"] <= limite_superior)]

# Mostrar resultados 
# Ver explicación fórmula cálculos
print("Q1 (25%):", q1)
print("Q2 (Mediana):", q2)
print("Q3 (75%):", q3)
print("IQR:", iqr)
print("Límite inferior:", limite_inferior)
print("Límite superior:", limite_superior)
print("\nDatos sin outliers en la columna 'Carnes':")
print(df_sin_outliers)


import matplotlib.pyplot as plt
import seaborn as sns

# Estilo estético
sns.set_theme(style="whitegrid")



# Crear la figura del boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, y="Carnes", color="lightblue")

# Título y etiquetas
plt.title("Boxplot de Gastos en Carnes")
plt.ylabel("Valor en pesos")

# Mostrar el gráfico
plt.show()