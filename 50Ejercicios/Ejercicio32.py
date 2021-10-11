num=int(input("Introduce un año: "))
if num%4==0 and num%100==0:
    print(num,"Es un año bisiesto")
else:
    print("No es bisiesto")
if num%400==0:
    print(num,"Es año bisiesto")
else:
    print(num,"No es un año bisiesto")