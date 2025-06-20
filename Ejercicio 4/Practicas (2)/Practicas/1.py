import pandas as pd

df = pd.read_excel("Mercado_casa.xlsx")

#Limpieza de datos nulos

df_sin_nulos = df.dropna(how="all")

print(df_sin_nulos)

#🔍 ¿Qué hace df.dropna(how="all")?
#Elimina solo aquellas filas donde _todos los valores_** sean NaN (nulos)**.

df_sin_nulos1 = df.dropna()

print(df_sin_nulos1)

#🔍 ¿Qué hace df.dropna()?
#Elimina todas las filas donde donde hay valores NaN (nulos)**.

df_sin_nulos2 = df.dropna(how="all")
df_sin_nulos3 = df_sin_nulos2.fillna(-1)
print(df_sin_nulos3)

#✅ Reemplazar todos los valores nulos (NaN) del DataFrame df_sin_nulos3 por el valor -1.
#🧠 ¿Para qué sirve esto?
#Este tipo de reemplazo es útil cuando quieres mantener todas las filas pero marcar los valores faltantes con un número especial que: 
#No se confunda con los datos reales (por eso se usa -1)
#Permita hacer análisis sin errores por nulos
#Sirva como código o bandera para detectar “dato no disponible”

