#Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora para calcular el salario bruto. Si la cantidad de horas excede las 40, deberá sumarle 1.5 veces el valor a las horas adicionales.
horas = int(input("Ingrese la cantidad de horas: "))
pxh = float(input("Ingrese el precio por hora: "))

if(horas > 40):
    totalpago = (40 * pxh) + (horas - 40) * pxh * 1.5
else:
    totalpago = horas*pxh

print("Total a pagar:", totalpago)
