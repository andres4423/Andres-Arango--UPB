num=int(input("Dame un número: "))
while num%2==0:
    print(num)
    if num<0:
        print("Es par negativo")
    else:
        print("Es par positivo")
        break
while num%2!=0:
    print(num)
    if num<0:
        print("Impar negativo")
    else:
        print("Impar positivo")
        break