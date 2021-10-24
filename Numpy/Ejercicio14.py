print("Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees. Centigrade values are stored into a NumPy array.")
print("Sample Array [0, 12, 45.21 ,34, 99.91] Expected Output: Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91] Values in Centigrade degrees: [-17.77777778 -11.11111111 7.33888889 1.11111111 37.72777778]")
print("Escriba un programa NumPy para convertir los valores de grados centígrados en grados Fahrenheit. Los valores en grados centígrados se almacenan en una matriz NumPy.")
print("Matriz de muestra [0, 12, 45.21, 34, 99.91] Salida esperada: Valores en grados Fahrenheit: [0. 12. 45.21 34. 99.91] Valores en grados centígrados: [-17.77777778 -11.11111111 7.33888889 1.11111111 37.72777778]")
import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
print(5*F/9 - 5*32/9)