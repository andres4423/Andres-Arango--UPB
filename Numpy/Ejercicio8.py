print("Write a NumPy program to create a 2d array with 1 on the border and 0 inside.")
print("Expected Output: Original array: [[ 1. 1. 1. 1. 1.] ................... [ 1. 1. 1. 1. 1.]]1 on the border and 0 inside in the array[[ 1. 1. 1. 1. 1.]................... [ 1. 1. 1. 1. 1.]]")
print("Escriba un programa NumPy para crear una matriz 2d con 1 en el borde y 0 en el interior.")
print("Resultado esperado: Matriz original: [[1. 1. 1. 1. 1.] ................... [1. 1. 1. 1. 1.] ] 1 en el borde y 0 en el interior de la matriz [[1. 1. 1. 1. 1.] ................... [1. 1. 1. 1. 1.]]")
import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)