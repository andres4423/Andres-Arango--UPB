print("Write a NumPy program to construct an array by repeating")
print("Sample array: [1, 2, 3, 4] Expected Output: Original array [1, 2, 3, 4] Repeating 2 times [1 2 3 4 1 2 3 4] Repeating 3 times [1 2 3 4 1 2 3 4 1 2 3 4]")
print("Escriba un programa NumPy para construir una matriz repitiendo")
print("Matriz de muestra: [1, 2, 3, 4] Resultado esperado: Matriz original [1, 2, 3, 4] Repitiendo 2 veces [1 2 3 4 1 2 3 4] Repitiendo 3 veces [1 2 3 4 1 2 3 4 1 2 3 4]")
import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)
print("Repeating 2 times")
x = np.tile(a, 2)
print(x)
print("Repeating 3 times")
x = np.tile(a, 3)
print(x)