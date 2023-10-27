#Utilice una lista para pedir la altura de los jugadores de un equipo de Volley y mostrar el promedio de altura.
alturas = []

while True:
    altura = float(input("Ingrese la altura de un jugador o 0 para terminar la carga: "))
    if altura != 0:
        alturas.append(altura)
    else:
        break
        
suma = 0
contador = len(alturas)
for i in alturas:
    suma = suma + i    

print ("La lista de jugadores es: ", alturas)
print (f"El promedio de altura de los jugadores es: {round(suma/contador, 2)}")