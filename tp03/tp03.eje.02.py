#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#2) Dado un número natural x, mostrar todos sus dígitos del menos significativo al más significativo.

numero = input("Dame un número entero: ")

if numero.isnumeric():
    numero = int(numero)
    print ("Los dígitos del número: " +  str(numero) +  " son: ")
    while numero > 0:
        print (numero%10)
        numero = numero // 10
else:
    print ("Ha ingresado una cadena.")