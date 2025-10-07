import pandas as pd

# Crear un DataFrame con datos ficticios
productos = {
    'Producto': ['Portátil', 'Ratón', 'Teclado', 'Monitor'],
    'Precio (€)': [1200, 25, 60, 200],
    'Unidades Vendidas': [15, 200, 150, 40]
}

df = pd.DataFrame(productos)
print(" Tabla de productos:\n", df)

# Seleccionar una columna
print("\nColumna 'Precio (€)':\n", df['Precio (€)'])

# Filtrar productos con precio mayor a 100 €
print("\nProductos con precio > 100 €:\n", df[df['Precio (€)'] > 100])

# Calcular el precio medio
print("\nPrecio medio:", df['Precio (€)'].mean())

# Ordenar por unidades vendidas (descendente)
print("\nProductos ordenados por unidades vendidas:\n", df.sort_values('Unidades Vendidas', ascending=False))
