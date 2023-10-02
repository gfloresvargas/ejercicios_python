#trabajo práctico nro 3 - variables simples
#autor: gustavo flores vargas
#fecha: 18/06/2023

#9) Dado un número natural x, mostrar todos sus divisores.
numero = input("Dame un número: ")
try:
    numero = int (numero)
except:
    print ("Ingrese un número.")
else:
    print (f"Los divisores del número {numero} son: ", end="")
    i = 1
    while (i <= numero-1):
        if (numero%i == 0):
            #print(i, sep=", ", end="")
            print(i, end=", ")
        i+=1
    print (numero)