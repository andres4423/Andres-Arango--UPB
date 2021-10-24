print("Write a NumPy program to append values to the end of an array.")
print("Expected Output: Original array: [10, 20, 30] After append values to the end of the array: [10 20 30 40 50 60 70 80 90]")
print("Escriba un programa NumPy para agregar valores al final de una matriz.")
print("Resultado esperado: Matriz original: [10, 20, 30] Después de agregar valores al final de la matriz: [10 20 30 40 50 60 70 80 90]")
import numpy as np
x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x, [[40, 50, 60], [70, 80, 90]])
print("After append values to the end of the array:")
print(x)