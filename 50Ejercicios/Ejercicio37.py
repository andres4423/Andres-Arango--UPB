num = input("Por favor ingrese 3 números separandolos con comas(,): ")
num = num.split(",")

if float(num[0]) < float(num[1]) and float(num[1]) < float(num [2]):
    print("Los números ingresados estan incrementandose.")

elif float(num[0]) > float(num[1]) and float(num[1]) > float(num[2]):
    print("Los números ingresados estan disminuyendose.")

else:
    print("Los números ingresados ni se incrementan ni se disminuyen.")