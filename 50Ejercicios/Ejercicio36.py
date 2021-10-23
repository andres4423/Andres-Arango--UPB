digito = input("Por favor ingrese un número: ")

digi1 = digito.split(".")
digi1 = int("".join(digi1))

if digi1 < 100000:
    print(digito, "tiene", len(str(digi1)),"digitos.")

else:
    print("El número ingresado es mayor que 100.000.")