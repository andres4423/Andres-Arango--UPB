print("Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.")
print("Expected Output: Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]")
print("Escriba un programa NumPy para convertir una lista de valores numéricos en una matriz NumPy unidimensional.")
print("Salida esperada: Lista original: [12.23, 13.32, 100, 36.32] Matriz NumPy unidimensional: [12.23 13.32 100. 36.32]")
import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)

