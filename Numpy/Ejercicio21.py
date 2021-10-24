print("Write a NumPy program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays.")
print("Array1: [ 0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70] Unique values that are in only one (not both) of the input arrays: [ 0 20 30 50 60 70 80]")
print("Escriba un programa NumPy para encontrar el conjunto exclusivo-o de dos matrices. Set exclusive-or devolverá los valores únicos ordenados que están en solo una (no ambas) de las matrices de entrada.")
print("Array1: [0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70] Valores únicos que están en solo uno (no en ambos) de los arreglos de entrada: [0 20 30 50 60 70 80]")
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(array1, array2))