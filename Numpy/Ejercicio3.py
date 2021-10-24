print("Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.")
print("Expected Output: \n [[ 2 3 4][ 5 6 7] [ 8 9 10]]")
print("Escriba un programa NumPy para crear una matriz de 3x3 con valores que van de 2 a 10")
print("Resultado esperado: \ n [[2 3 4] [5 6 7] [8 9 10]]")

import numpy as np
x =  np.arange(2, 11).reshape(3,3)
print(x)