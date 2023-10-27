#Dados dos números enteros positivos menores a 100, mostrar todos los números naturales en ese rango.
menor = int(input("Ingrese el valor inferior del rango: "))
mayor = int(input("Ingrese el valor superior del rango: "))

#para que siempre se contabilice el menor primero y el mayor después
if menor > mayor:
    aux = menor
    menor = mayor
    mayor = aux

for i in range(menor, mayor + 1):
    print (i)