1. Ejercicio 1
def correo(email):
    for a in email:
        if a == "@":
            print("Email valido")
        else:
            print("Email invalido")
       a
correo(input("Dame tu correo electronico"))

Solución Andrés Leon:
def validar(email):
    b=a.count("@")
    if b==1:
        return True
    return False

a=input("Introduce tu email")
if validar(a):
    print("Dirección válida")
else:
    print("Dirección inválida")
    print("Por favor ingrese su email con @")

#Solución Jerson Arley
def validar(email):
    respuesta=False
    if "@" in email:
        respuesta=True
    return respuesta
direccion=input("Tu email: ")
if validar(direccion):
    print("Direccion valida")
else:
    print("Direccion invalida")

#Ejercicio 2
def sumaDigitos(numero)
numero=int(input("Ingrese un numero: ")
    suma=0
    for i in range(numero):
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
num=int(input("Número a procesar, si quiere finalizar ingrese el numero 0: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar, si quiere finalizar ingrese el numero 0: "))

#Solución Alexandra Bernal
num=int(input("Ingrese el numero que quiere procesar: "))
def sumaDigitos(num):
    suma=0
    while num !=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

while num!=0:
    print("La suma de los digitos es:",sumaDigitos(num))
    num=int(input("Ingrese otro número, si quiere finalizar el proceso ingrese un cero: " ))
    print("El proceso ha finalizado")

#Ejercicio 3
def sumaDig(numero):
    suma=0
    for i in range(numero):
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
sumatoria=0
num=int(input("Numero a procesar, para finalizar ingresar 0"))
while num!=0:
    print("Suma:",sumaDig(num))
    sumTotal=sumatoria+num
    num=int(input("Numero a procesar para finalizar ingrese 0:"))
print("Sumatoria:",sumatoria)
print("Digitos",sumaDig(sumatoria))
print("Acaba la operacion")

Ejercicio 4
cond="si"

def primo(num):
   for i in range(2,num):
       while num%i==0:           
           return False

   return True
while cond == "si":
    numero=int(input("ingrese un Número: "))
    if primo(numero):
        print("Es primo")
    else:
        print("No es primo")
    cond=input("¿quieres ingresar otro Número? ")
    if cond == "no":
        print("hasta luego, vuelva pronto.")

Ejercicio 5
cond="si"
def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad
if cond=="si":
    num=int(input("ingrese un Número: "))
    un_digito=int(input("ingrese un Dígito: "))
    print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))
    cond=input("quieres volver a ingresar un numero y un digito = ¿si o no?")
if cond=="no":
    print("vuelve pronto amigo....(saludos desde Tibú)")

Ejercicio 6

def factorial(numero):
   f=1
   if numero==1:
       return 1
    else:
          return numero*factorial(numero-1)
cantidad=0
num=int(input("ingrese un Número, si quiere terminar ingrese un -1 para cortar: "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("ingrese un Número, si quiere terminar ingrese un -1 para cortar: "))
else: 
    print("Se leyeron",cantidad,"números ingresados")

Ejercicio 7:
def sumaDigitos(numero):
    suma=0
    for i in range(0,numero):
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
            suma=sumaDigitos(numero)
           if suma > mayor:
                mayor=suma
                n_mayorsuma=numero
           if suma < 10:
                cantidad+=1
            print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
            print("Cantidad con sumatoria menor a 10:",cantidad)               
          else:
            print("el numero ingresado es incorrecto")

Ejercicio 8:
def primo(num): 
   for i in range(2,num): 
       if num%i==0:            
           return False 
   return True 
def frecuencia(numero,digito): 
   cantidad=0 
   while numero!=0: 
       ultDigito=numero%10 
       if ultDigito==digito: 
           cantidad+=1 
       numero=numero//10 
   return cantidad 
def factorial(numero): 
   f=1 
   if numero!=0: 
       for i in range(1,numero+1): 
           f=f*i 
   return f 
def sumaDigitos(numero): 
  suma=0 
  while numero!=0: 
      digito=numero%10 
      suma=suma+digito 
      numero=numero//10 
  return suma 
mayor=0 
agregar = "si" 
while agregar == "si": 
    numero=int(input("Ingrese un número primo: ")) 
    while primo(numero): 
        digito=int(input("Dígito: ")) 
        print("Suma de los dígitos:",sumaDigitos(numero)) 
        print("El",digito,"aparece",frecuencia(numero,digito),"veces") 
        if numero > mayor: 
            mayor=numero 
        break 
    else: 
        print("Factorial de",mayor,":",factorial(mayor)) 
        print("El últmo número ingresado no es primo.") 
        print("El programa ha finalizado con éxito") 
        break 
    agregar = input("¿Quiere ingresar otro número? si o no = ") 
    if agregar == "no": 
        print("Factorial de",mayor,":",factorial(mayor)) 
        print("El programa ha finalizado con éxito.") 
        break 


Ejercicio 9:

y=2
def f(num):
   cantidad=0
   while num!=0:
       Dig=num%10
       cantidad+=1
       num=num//10
   return cantidad
while y==2:
    hi=input("""que desea ingresar:
    1.Cedula de ciudadania
    2.Tarjeta de identidad
    """)
    num=int(input("ingrese el numero: "))
    if f(num)>10 and f(num)<10:
        print("El número es invalido")
    elif f(num)==10:
        print("Número es valido")
    else:
        print("El número es invalido")
    break 


#Ejercicio 10:
cantidad=0
def lenUltimaPalabra(cadena):
   if len(cadena)==0:
       return 0
   for i in range(len(cadena)):
       if cadena[i]!=' ':
           cantidad+=1
       else:
           if i<len(cadena)-1 and cadena[i+1]!=' ':
               cantidad=0
   return cantidad
cadena = input("Ingrese la cadena o frase = ")
if lenUltimaPalabra(cadena):
    print(lenUltimaPalabra(cadena))



Ejercicio aparte-> Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.
def funcion(*nums):
    suma=0
    for i in nums:
       suma+=i 
    return suma
print(funcion(2,4,5,1))

def funcion(*nums):
    mult=1
    for i in nums:
       mult=mult*i 
    return mult
print(funcion(2,4,2,2))

def func(num):
        if num >=1:
            print(num)
            func(num-1)
func(5)

def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)

# Ejecutamos la función
pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')  
