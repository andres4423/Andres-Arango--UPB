notas = []
contador = 0

while contador < 5:
    nota = float(input("Por favor ingrese la nota del estudiante: "))
    if nota < 0.0 or nota > 5.0:
        break
    notas.append(nota) 
    contador +=1

notafinal = notas[0]*0.15 + notas[1]*0.2 + notas[2]*0.15 + notas[3]*0.3 + notas[4]*0.2
if 2.0 <= notafinal < 3.0: 
    print("La nota final del etudiante es:","{0:.2f}".format(notafinal),"por lo que el estudiante reprobó el curso.") 
elif notafinal < 2.0:
    print("La nota final del etudiante es:","{0:.2f}".format(notafinal),"por lo que el estudiante reprobó el curso y no podra habilitar.")

else:
    print("La nota final del etudiante es:","{0:.2f}".format(notafinal),"por lo que el estudiante aprobó el curso.")
    if notafinal > 4.5:
        print("Felicitaciones por tu esfuerzo, sigue así.")