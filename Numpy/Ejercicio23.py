print("Write a NumPy program to test whether all elements in an array evaluate to True")
print("Note: 0 evaluates to False in NumPy.")
print("Escriba un programa NumPy para probar si todos los elementos de una matriz se evalúan como True")
print("Nota: 0 se evalúa como Falso en NumPy.")
import numpy as np
print(np.all([[True,False],[True,True]]))
print(np.all([[True,True],[True,True]]))
print(np.all([10, 20, 0, -50]))
print(np.all([10, 20, -50]))