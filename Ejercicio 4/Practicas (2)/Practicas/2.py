import pandas as pd

# Crear DataFrame original con una fila duplicada
df_original = pd.DataFrame({
    "Año": [2024, 2024, 2024],
    "Mes": ["Ene", "Feb", "Feb"],
    "Víveres": [200000, 210000, 210000],
    "Verduras": [60000, 65000, 65000]
})

print("📌 DataFrame original:")
print(df_original)

# Eliminar duplicados
df_sin_duplicados = df_original.drop_duplicates()

print("\n✅ DataFrame después de aplicar .drop_duplicates():")
print(df_sin_duplicados)
