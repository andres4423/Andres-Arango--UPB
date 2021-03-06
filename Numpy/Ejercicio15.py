print("Escriba un programa NumPy para encontrar las partes reales e imaginarias de una matriz de números complejos.")
print("Expected Output: Original array [ 1.00000000+0.j 0.70710678+0.70710678j] Real part of the array: [ 1. 0.70710678] Imaginary part of the array: [ 0. 0.70710678]")
print("Escriba un programa NumPy para encontrar las partes reales e imaginarias de una matriz de números complejos.")
print("Salida esperada: matriz original [1.00000000 + 0.j 0.70710678 + 0.70710678j] Parte real de la matriz: [1. 0.70710678] Parte imaginaria de la matriz: [0. 0.70710678]")
import numpy as np
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)