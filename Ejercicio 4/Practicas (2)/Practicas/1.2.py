import pandas as pd

df = pd.read_excel("Mercado_casa.xlsx")

#Limpieza de datos nulos

df_sin_nulos1 = df.dropna()

print(df_sin_nulos1)