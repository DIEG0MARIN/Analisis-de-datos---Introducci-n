import pandas as pd

df = pd.read_csv("datos_ejemplo.csv")

#Calcular media
print("Media de edad:", df["Edad"].mean())

#Calcular mediana y moda
print("El valor de la Mediana es:", df["Calificación"].median())
print("El valor de la Moda es:", df["Calificación"].mode()[0])


#Calcular la mediana de edades

print("La mediana de edades es:", df["Edad"].median())