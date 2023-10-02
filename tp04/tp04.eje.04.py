#trabajo práctico nro 4 - “Estructuras de Control: Condicionales, Ciclos, Excepciones”
#autor: gustavo flores vargas
#fecha: 26/06/2023

#4) Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

puntuacion = round(float(input("Ingrese una puntuación entre [0.0] - [1.0]: ")), 2)

if (puntuacion >= 0) and (puntuacion <= 1.0):
    print ("Puntuación Calificación")
    if (puntuacion >= 0.9):
        print ("Sobresaliente")
    elif (puntuacion >= 0.8):
        print ("Notable")
    elif (puntuacion >= 0.7):
        print ("Bien")
    elif (puntuacion >= 0.6):
        print ("Suficiente")
    else:
        print ("Insuficiente")
else:
    print ("Error. La puntuación no conicide con la solicitada.")

