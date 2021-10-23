num=int(input("Dame un número: "))
if num<0 and num>10:
    print("Número invalido")
elif num==1:
    print(num,"-->UNO")
elif num==2:
    print(num, "-->DOS")
elif num==3:
    print(num,"-->TRES")
elif num==4:
    print(num,"-->CUATRO")
elif num==5:
    print(num,"-->CINCO")
elif num==6:
    print(num,"-->SEIS")
elif num==7:
    print(num,"-->SIETE")
elif num==8:
    print(num,"-->OCHO")
elif num==9:
    print(num,"-->NUEVE")
else:
    print(num,"-->DIEZ")