a = 0
b = 0
pn = int(input("Ingrese cuantos numeros quiere ingresar: "))
for i in range(pn):
    p1 = int(input("Ingrese un número: "))
    if p1 >= 100:
      a += 1
    else:
        b += 1
print("números mayores a 100: ", a, "\nnúmeros menores a 100: ", b)
