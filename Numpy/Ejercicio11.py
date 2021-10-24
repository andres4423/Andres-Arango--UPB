print("Write a NumPy program to convert a list and tuple into arrays.")
print("List to array: [1 2 3 4 5 6 7 8] Tuple to array: [[8 4 6] [1 2 3]]")
print("Escriba un programa NumPy para convertir una lista y una tupla en matrices.")
print("Lista a matriz: [1 2 3 4 5 6 7 8] Tupla a matriz: [[8 4 6] [1 2 3]]")
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(my_tuple))