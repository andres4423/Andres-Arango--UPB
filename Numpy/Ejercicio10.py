print("Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.")
print("Checkerboard pattern: [[0 1 0 1 0 1 0 1] .......... [0 1 0 1 0 1 0 1][1 0 1 0 1 0 1 0]]")
print("Escriba un programa NumPy para crear una matriz de 8x8 y rellénela con un patrón de tablero de ajedrez.")
print("Patrón de tablero de ajedrez: [[0 1 0 1 0 1 0 1] .......... [0 1 0 1 0 1 0 1] [1 0 1 0 1 0 1 0]]")
import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)