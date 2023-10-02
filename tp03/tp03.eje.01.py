#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#1) Dado un número natural x, mostrar su último dígito.

numero = input("Dame un número entero: ")
if (type(numero) == int):
    print ("El último número ingresado es: " +  str(numero%10))
elif numero.isnumeric():
    print ("El último número ingresado es: " +  numero[-1])
else:
    print ("Ha ingresado una cadena.")