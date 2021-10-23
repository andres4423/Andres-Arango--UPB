Sum = 0 
Cont = 0
while Cont < 10: 
    numero = float(input("Por favor ingrese un número: ")) 
    if numero == 0: 
        continue 
    Sum += numero 
    Cont += 1  
    Prom = Sum / Cont
    
print("La suma de los 10 números ingresados es: ", (Sum))
print("El promedio de los 10 números ingresados es:", (Prom))