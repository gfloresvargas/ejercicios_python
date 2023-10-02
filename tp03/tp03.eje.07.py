#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#7) Dado un número ontero x, mostrar sus n primeras potencias
#se debe indicar el número x  luego sus potencias naturales

numero = input("dame un número: ")
potencia = input("dame la potencia: ")
contador = 0
if (numero.isnumeric()) and (potencia.isnumeric()):
    numero =int(numero)
    potencia = int(potencia)
    contador = int(contador)
    print ("Las primeras " + str(potencia) + " potencias de " + str(numero) + " son: ")
    while contador < potencia:
        print (numero ** contador)
        contador += 1
else:
    print ("Ha ingresado una cadena.")