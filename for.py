#Ejercicio 1:
for num in range(0,10):
    #print(num)

#Ejercicio 2:    
 for n in range(100,200):
    print(n)

#Ejercicio 3:
for c in range(5,21,3):
    print(c)

#Ejercicio 4:
num=int(input("Ingresa un numero"))
for n in range(num, num*2):
     print(n)

#Ejercicio 5:
frase=input("Ingresa una frase")
for n in "aeiou":
    if n in frase.lower():
        print(n)
        
#Ejercicio 7:
for i in range(0,100):
    i+=i
    print(i)



#Ejercicio 9:
num=int(input("Número: "))
f=1
if num !=0:
    for i in range(1,num+1):
        f=f*1
        print("Factorial",i)
