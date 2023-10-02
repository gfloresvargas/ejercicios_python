#trabajo práctico nro 4 - “Estructuras de Control: Condicionales, Ciclos, Excepciones”
#autor: gustavo flores vargas
#fecha: 26/06/2023

#2)Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

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
        
