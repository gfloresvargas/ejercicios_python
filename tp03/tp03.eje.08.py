#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#8) Dado un número entero x, calcular x^y y mostrar el resultado.
numero = input("Dame un número: ")
potencia = input("Dame la potencia: ")

if (numero.isnumeric()) and (potencia.isnumeric()):
    numero =int(numero)
    potencia = int(potencia)
    print (str(numero) + " elevado a su " + str(potencia) + " potencia es: " + str(numero ** potencia))
else:
    print ("Ha ingresado una cadena.")