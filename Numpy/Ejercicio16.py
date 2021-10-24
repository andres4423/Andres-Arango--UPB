print("Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.")
print("Expected Output: Size of the array: 3 Length of one array element in bytes: 8 Total bytes consumed by the elements of the array: 24")
print("Escriba un programa NumPy para encontrar el número de elementos de una matriz, la longitud de un elemento de la matriz en bytes y el total de bytes consumidos por los elementos.")
print("Salida esperada: Tamaño de la matriz: 3 Longitud de un elemento de la matriz en bytes: 8 Total de bytes consumidos por los elementos de la matriz: 24")
import numpy as np
x = np.array([1,2,3], dtype=np.float64)
print("Size of the array: ", x.size)
print("Length of one array element in bytes: ", x.itemsize)
print("Total bytes consumed by the elements of the array: ", x.nbytes)
