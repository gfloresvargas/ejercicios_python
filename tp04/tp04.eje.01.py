#trabajo práctico nro 4 - “Estructuras de Control: Condicionales, Ciclos, Excepciones”
#autor: gustavo flores vargas
#fecha: 26/06/2023

#1) Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora para calcular el salario bruto.

horas = int(input("Ingrese las horas de trabajo: "))
tarifa = round(float(input("Ingrese la tarifa $: ")), 2)
print ("Ingrese un valor numerico.")

print (f"El salario bruto es: $ {horas * tarifa}")
