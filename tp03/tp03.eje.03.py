#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#3) Dado un número natural x, contar la cantidad de dígitos que posee.
numero = input("Dame un número natural: ")
digitos = 0

if numero.isnumeric():
    numero = int(numero)
    print ("Los dígitos del número: " +  str(numero) +  " son: ")
    while numero > 0:
        digitos += 1
        numero = numero // 10
    print ("La cantidad de dígitos es: " + str(digitos))
else:
    print ("Ha ingresado una cadena.")