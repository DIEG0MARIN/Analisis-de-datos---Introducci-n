import numpy as np

vector = np.array([1, 2, 3, 4, 5])


media = np.mean(vector)
print("La media es: ", media)


desviacionEstandar = np.std(vector)
print("La desviación estanadar es: ", round(desviacionEstandar, 3))


#CREAR UNA MATRIZ DE 3X2


matriz = np.random.randint(1, 11, size=(3, 2))

print("Matriz 3x2 con números aleatorios:")
print(matriz)

#   MULTIPLICAR LA MATRIZ POR UN ESCALAR
escalar = 2
matrizEscalar = matriz * escalar
print("Matriz multiplicada por el escalar 2:", matrizEscalar)

