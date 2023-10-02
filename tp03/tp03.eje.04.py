#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#4) Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.
numero = input("Dame un número entero: ")
pares = 0
impares = 0

if numero.isnumeric():
    numero = int(numero)
    while numero > 0:
        if int((numero%10)%2) == 0:
            pares += 1
        else:
            impares += 1
        numero = numero // 10
    print ("La cantidad de dígitos son: pares " +  str(pares) +  ", impares " + str(impares) + ".")
else:
    print ("Ha ingresado una cadena.")