import math
punto1= input("Ingrese coordenada de primer punto: ")
punto2= input("Ingrese coordenada segundo punto: ")

p1= punto1.split((","))
p2= punto2.split((","))

x1=eval(p1[0])
y1=eval(p1[1])
x2=eval(p1[0])
y2=eval(p1[1])

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("La distancia entre los dos puntos es= {:.2f}".format(distancia))