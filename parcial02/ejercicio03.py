#Dado el radio de un círculo, calcule el área del mismo. Use la constante Pi con 4 dígitos. Muestre el resultado con 2 dígitos.
r = float(input("Ingrese el radio del circulo: "))
pi = 3.1416
area = round(pi*r**2,2)
print("El area del circulo es:", area)
