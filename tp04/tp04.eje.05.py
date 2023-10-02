#trabajo práctico nro 4 - “Estructuras de Control: Condicionales, Ciclos, Excepciones”
#autor: gustavo flores vargas
#fecha: 26/06/2023

#5) Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, detecta su fallo usando try y except, muestra un mensaje de error y pasa al número siguiente.
suma = 0
cantidad = 0
numero = 0

while (numero != "fin"):
    numero = input("Dame un numero [<fin> para termina]: ")
    try:
        numero = int(numero)
        suma = suma + numero
        cantidad = cantidad + 1
    except:
        print ("Error, ingrese un número.")

print ("Resultado: ", suma)
print ("Promedio: ", suma/cantidad)