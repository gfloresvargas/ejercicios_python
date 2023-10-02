#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#6) Dado un número natural x, determinar si es capicúa.
numero = input("Dame un número natural: ")
if numero.isnumeric():
    reversa= 0
    original = int(numero)
    numero = int(numero)
    while numero > 0:
        reversa = reversa * 10 + int(numero%10)
        numero = numero // 10
    if reversa == original:
        print ("El número " +  str(original) +  " es capicúa.")
    else:
        print ("El número ingresado no es capicúa.")
else:
    print ("Ha ingresado una cadena.")