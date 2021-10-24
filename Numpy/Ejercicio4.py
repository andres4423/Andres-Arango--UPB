print("Write a NumPy program to create a null vector of size 10 and update sixth value to 11")
print("[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]")
print("Escriba un programa NumPy para crear un vector nulo de tamaño 10 y actualice el sexto valor a 11.")
print("[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] Actualiza el sexto valor a 11 [0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]")
import numpy as np
x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)