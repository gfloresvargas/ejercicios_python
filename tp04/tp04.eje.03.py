#trabajo práctico nro 4 - “Estructuras de Control: Condicionales, Ciclos, Excepciones”
#autor: gustavo flores vargas
#fecha: 26/09/2023

#3) Vuelva a reescribir el programa del salario usando try y except, de modo que el programa sea capaz de gestionar entradas no numéricas con elegancia, 
#mostrando un mensaje y saliendo del programa. A continuación se muestra un ejemplo de ejecución.

while True:
    try:
        horas = int(input("Ingrese las horas de trabajo: "))
        tarifa = int(input("Ingrese la tarifa $: "))
    except ValueError:
        print ("Ingrese un valor numérico.")
    else:
        break

#una vez que se obtuvo exitosamente ambos registros, multiplir por 1.5 veces
if (horas > 40):
    salario = (horas * tarifa) * 1.50
else:
    salario = (horas * tarifa)

print (f"El salario bruto es: $ {salario}")
