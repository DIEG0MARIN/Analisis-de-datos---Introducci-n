import pandas as pd

df = pd.read_excel("Mercado_casa.xlsx")

#Limpieza de datos nulos

df_sin_nulos2 = df.dropna(how="all")
df_sin_nulos3 = df_sin_nulos2.fillna(-1)
print(df_sin_nulos2)
print(df_sin_nulos3)