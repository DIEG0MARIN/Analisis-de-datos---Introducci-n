# Importar pandas para manipulación de datos
import pandas as pd

# Cargar el archivo Excel desde la hoja 'Datos'
df_original = pd.read_excel("LimpiezaOrtografia.xlsx", sheet_name="Datos")

# Crear una copia del DataFrame original para no modificarlo directamente
df = df_original.copy()

# --------------------------------------------
# 🔹 LIMPIEZA DE DATOS CATEGÓRICOS (COLUMNA 'Ciudad')
# --------------------------------------------

# Convertir todos los valores de la columna 'Ciudad' a mayúsculas
df["Ciudad"] = df["Ciudad"].str.upper()

# Reemplazar variantes inconsistentes para estandarizar nombres de ciudades
df["Ciudad"] = df["Ciudad"].replace({
    "BOGOTA": "BOGOTÁ",        # Añadir tilde para unificar
    "MEDELLIN": "MEDELLÍN"     # Añadir tilde
    # Puedes agregar más reglas si encuentras otras variantes
})

# --------------------------------------------
# 🔹 AGRUPACIÓN DE DATOS
# --------------------------------------------

# Agrupar por ciudad y sumar el valor de facturación total por ciudad
df_agrupado = df.groupby("Ciudad")["ValorFactura"].sum().reset_index()

# --------------------------------------------
# 🔹 RESULTADO FINAL
# --------------------------------------------

# Imprimir la tabla agrupada ya limpia y corregida
print("Valor total facturado por ciudad (con nombres normalizados):")
print(df_agrupado)
