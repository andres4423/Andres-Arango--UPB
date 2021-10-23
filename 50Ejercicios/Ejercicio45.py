num = int(input("Por favor ingresa un número: "))

contador = 0
numeros = []
while contador < num:
    contador += 1
    if contador % 2 == 0:
        cont1 = contador * -1
        numeros.append(cont1)
    else:
        numeros.append(contador)

print(" ")
print(numeros)