import numpy as np

# Crear un array 2D (matriz) con números enteros
matriz = np.array([[10, 20, 30], [40, 50, 60]])
print("Matriz original:\n", matriz)

# Sumar un valor a toda la matriz
print("\nMatriz + 10:\n", matriz + 10)

# Multiplicar por 2
print("\nMatriz * 2:\n", matriz * 2)

# Seleccionar la primera fila
print("\nSegundo elemento de la primera matriz:\n", matriz[0][1])

# Calcular la media de todos los valores
print("\nMedia de la matriz:", matriz.mean())
