venta=float(input("Valor de la venta: "))
iva=float(venta*0.19)
valorTotal=float(venta+iva)
if venta>=150.000:
    valorTotal=float(valorTotal-0.05)
else:
    print("El valor de la venta original es: ",venta)
print("El valor total de la venta es: ",valorTotal)
