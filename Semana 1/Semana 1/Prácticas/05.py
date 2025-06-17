def calcular_dato_faltante(valores, media_esperada):
    """
    Calcula el valor faltante en una lista con un solo dato desconocido (representado por None).
    
    :param valores: Lista de números, usando None donde falta el valor.
    :param media_esperada: Valor de la media aritmética conocida.
    :return: Valor faltante.
    """
    n = len(valores)
    suma_esperada = media_esperada * n
    suma_conocida = sum(v for v in valores if v is not None)
    dato_faltante = suma_esperada - suma_conocida
    return dato_faltante

# Ejemplo: [4, 5, 13, X], media esperada = 7
valores = [4, 5, 13, None]
media_esperada = 7

faltante = calcular_dato_faltante(valores, media_esperada)
print(f"El dato faltante es: {faltante}")
