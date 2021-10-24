print("Write a NumPy program to get the unique elements of an array.")
print("Expected Output: Original array: [10 10 20 20 30 30] Unique elements of the above array: [10 20 30] Original array: [[1 1] [2 3]] Unique elements of the above array: [1 2 3]")
print("Escriba un programa NumPy para obtener los elementos únicos de una matriz.")
print("Resultado esperado: Matriz original: [10 10 20 20 30 30] Elementos únicos de la matriz anterior: [10 20 30] Matriz original: [[1 1] [2 3]] Elementos únicos de la matriz anterior: [1 2 3 ]")
import numpy as np
x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
x = np.array([[1, 1], [2, 3]])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))