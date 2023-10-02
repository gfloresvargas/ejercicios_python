#trabajo práctico nro 2 - variables simples
#autor: gustavo flores vargas
#fecha: 30/08/2022

#11) Dado un número natural x, sumar todos sus divisores.
numero = input("Dame un número: ")
divisores = []
suma = 0
if (numero.isnumeric()):
    numero =int(numero)
    for i in range(1, numero+1, 2):
        if (numero%i == 0):
            divisores.append(i)
            suma += i
    #imprimir el total y la lista
    print("La suma de los divisores de: ", str(numero))
    print(divisores)
    print("es = " + str(suma))
else:
    print ("Ha ingresado una cadena.")
