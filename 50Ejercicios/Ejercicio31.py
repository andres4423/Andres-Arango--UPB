import datetime

distancia = float(input("Por favor ingresa la distancia a reccorrer de tu vuelo: "))
dias = int(input("Por favor ingresa el número de diás de estancia: "))
print(" ")
print("_______________________________________")

if distancia > 1000 and dias > 7:
    distancia *= 5000
    descuento = distancia * 0.15
    distan1 = distancia - descuento
    print("Valor original del vuelo: $", distancia)
    print("Valor del descuento: $", "{0:g}".format(descuento))
    print("Valor final del vuelo: $", distan1)

else:
    if distancia > 20:
        distancia *= 5000
        print("Valor del vuelo: $", "{0:g}".format(distancia))
    else:
        distan = 100000
        print("Valor del vuelo: $","{0:g}".format(distan))

print("Que tenga un buen viaje.")
print("Fecha: ",datetime.date.today())