#Cree una calculadora monetaria, que pida el tipo de cambio y luego muestre los siguientes menús, para obtener el resultado del cambio.
#1: Pesos a Dólares
#2: Dólares a Pesos
cotizacion = 1005
print("La cotización del día es: ", round(cotizacion, 2))
print("Opciones de cambio: ")
print("1: Pesos a Dólares")
print("2: Dólares a Pesos")
c = int(input("Bienvenido, ingrese un tipo de cambio: "))


if(c==1):
    pesos = int(input("Ingrese la cantidad de pesos: "))
    dolares = pesos/cotizacion
    print("El monto ingresado equivale a:", round(dolares, 2) ,"dólares")
elif(c==2):
    dolares = int(input("Ingrese la cantidad de dólares: "))
    pesos = dolares*cotizacion
    print("El monto ingresado equivale a:", round(pesos, 2), "pesos")
else:
    print("ERROR, opción inválida")