num1=int(input("Dame un número"))
num2=int(input("Dame otro número"))
num3=int(input("Dame un último número"))
if num1==num2:
    print(num1,"Es igual a",num2)
elif num2==num3:
    print(num2,"Es igual a",num3)
elif num1==num3:
    print(num1,"Es igual a",num3)
else:
    print("No hay numero iguales")