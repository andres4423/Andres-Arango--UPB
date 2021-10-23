num=int(input("Dame un número"))
while num%2==0:
    print("El número dado es: ",num, "par")
    if num<0:
        print("Número par negativo")
    else:
        print("Número par positivo")
    break

while num%2!=0:
    print("El número dado es: ",num, "impar")
    if num<0:
        print("Número impar negativo")
    else:
        print("Número impar positivo")
    break
