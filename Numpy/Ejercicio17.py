print("Write a NumPy program to test whether each element of a 1-D array is also present in a second array.")
print("Expected Output: Array1: [ 0 10 20 40 60] Array2: [0, 40] Compare each element of array1 and array2[ True False False True False]")
print("Escriba un programa NumPy para probar si cada elemento de una matriz 1-D también está presente en una segunda matriz.")
print("Resultado esperado: Array1: [0 10 20 40 60] Array2: [0, 40] Compare cada elemento de array1 y array2 [Verdadero Falso Falso Verdadero Falso]")

import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))