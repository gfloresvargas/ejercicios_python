#Pida el número de mes de nacimiento y muestre el nombre del mes en mayúscula.
mes = int(input("Ingrese su mes de nacimiento: "))
meses = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
if mes >= 1 and mes <= 12:
    print (f"Su mes de nacimiento es {meses[mes - 1]}")
else:
    print ("Ingrese un número de mes válido.")
