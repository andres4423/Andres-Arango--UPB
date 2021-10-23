r = input("Por favor ingrese el radio(r) del circulo en cm: ")
caracters = "cm"
for x in range(len(caracters)): 
    r = r.replace(caracters[x],"")
r = float(r)

p = 2* 3.1416 * r 
a = 3.1416 * r**2 

print("El area del  circulo es:", a ,"cm**2"+".")
print("El perimetro del circulo es:", p ,"cm"+".")