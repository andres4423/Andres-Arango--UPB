
print("Write a NumPy program to test whether any array element along a given axis evaluates to True")
print("Note: 0 evaluates to False in NumPy.")
print("Escriba un programa NumPy para probar si algún elemento de la matriz a lo largo de un eje dado se evalúa como Verdadero")
print("Nota: 0 se evalúa como Falso en NumPy.")
import numpy as np
print(np.any([[False,False],[False,False]]))
print(np.any([[True,True],[True,True]]))
print(np.any([10, 20, 0, -50]))
print(np.any([10, 20, -50]))