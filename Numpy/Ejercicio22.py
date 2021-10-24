print("Write a NumPy program to find the union of two arrays. Union will return the unique, sorted array of values that are in either of the two input arrays.")
print("Array1: [ 0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70] Unique sorted array of values that are in either of the two input arrays: [ 0 10 20 30 40 50 60 70 80]")
print("Escriba un programa NumPy para encontrar la unión de dos matrices. Union devolverá la matriz única y ordenada de valores que se encuentran en cualquiera de las dos matrices de entrada.")
print("Array1: [0 10 20 40 60 80] Array2: [10, 30, 40, 50, 70] Arreglo ordenado único de valores que se encuentran en cualquiera de los dos arreglos de entrada: [0 10 20 30 40 50 60 70 80]")
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique sorted array of values that are in either of the two input arrays:")
print(np.union1d(array1, array2))