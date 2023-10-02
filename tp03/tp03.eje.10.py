#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#10) Dado un número natural x, contar todos sus divisores.
numero = input("Dame un número: ")
try:
    numero =int(numero)
except:
    print ("Ha ingresado una cadena.")
else:
    i = 1
    cantidad = 0
    while (i <= numero):
        if (numero%i == 0):
            cantidad += 1
        i += 1
    print (f"El número {numero} tiene {cantidad} divisores.")
