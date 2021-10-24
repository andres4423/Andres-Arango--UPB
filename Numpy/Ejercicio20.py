print("Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.")
print("Expected Output: Array1: [ 0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70, 90] Set difference between two arrays: [ 0 20 60 80]")
print("Escriba un programa NumPy para encontrar la diferencia de conjuntos de dos matrices. La diferencia establecida devolverá los valores únicos ordenados en la matriz 1 que no están en la matriz2.")
print("Salida esperada: Matriz 1: [0 10 20 40 60 80] Matriz 2: [10, 30, 40, 50, 70, 90] Establecer la diferencia entre dos matrices: [0 20 60 80]")
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))