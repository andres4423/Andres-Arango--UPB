print("Write a NumPy program to create an empty and a full array.")
print("Expected Output: [ 6.93270651e-310 1.59262180e-316 6.93270559e-310 6.93270665e-310] [ 6.93270667e-310 6.93270671e-310 6.93270668e-310 6.93270483e-310] [ 6.93270668e-310 6.93270671e-310 6.93270370e-310 6.93270488e-310]] [[6 6 6] [6 6 6] [6 6 6]]")
print("Escriba un programa NumPy para crear una matriz vacía y completa.")
print("Salida esperada: [6.93270651e-310 1.59262180e-316 6.93270559e-310 6.93270665e-310] [6.93270667e-310 6.93270671e-310 6.93270668e-310 6.93270483e-310] [6.93270668e-310 6.932.932703e-310 -310 6.93270488e-310]] [[6 6 6] [6 6 6] [6 6 6]]")
import numpy as np
# Create an empty array
x = np.empty((3,4))
print(x)
# Create a full array
y = np.full((3,3),6)
print(y)