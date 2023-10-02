#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#5) Dado un número natural x, sumar todos sus dígitos. Mostar la suma obtenida.
numero = input("Dame un número natural: ")
digito = 0
suma = 0

if numero.isnumeric():
    numero = int(numero)
    while numero > 0:
        digito = int(numero%10)
        suma += digito
        numero = numero // 10
    print ("La suma de los dígitos es: " +  str(suma) +  ".")
else:
    print ("Ha ingresado una cadena.")