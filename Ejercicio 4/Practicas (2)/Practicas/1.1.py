import pandas as pd

df = pd.read_excel("Mercado_casa.xlsx")

#Limpieza de datos nulos

df_sin_nulos = df.dropna(how="all")

print(df_sin_nulos)

# En esta ocasión no elimino ningún dato porque no hay filas donde todos los datos sean nulos