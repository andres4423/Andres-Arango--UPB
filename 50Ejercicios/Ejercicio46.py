n = int(input("Por favor ingresa el primer número: "))
m = int(input("Por favor ingresa el segundo número: "))


if m < n:
    cont = n-1
    numeros = []
    while cont < m:
        cont += 1
        numeros.append(cont)
    print(" ")
    print(numeros)

else:
    print("El rango establecido es invalido.")