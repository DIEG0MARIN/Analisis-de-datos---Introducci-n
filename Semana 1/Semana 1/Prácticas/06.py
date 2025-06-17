# el primer paso es importar statistics
import statistics

# el segundo paso es guardar los numeros del arreglo en una variable

alturas = [8, 1, 2, 6, 1, 4]

media = statistics.mean(alturas)

mediana = statistics.median(alturas)

moda = statistics.mode(alturas)

print(f"La media de las alturas de las plantas es: {media}")
print(f"La mediana de las alturas de las plantas es: {mediana}")
print(f"La moda de las alturas de las plantas es: {moda}")