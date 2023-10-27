#Calcular el promedio de un alumno, dada 3 notas. Mostrar si está aprobado o en suspenso. La nota mínima para aprobar es 6.
nota01 = int(input("Ingrese la nota 01: "))
nota02 = int(input("Ingrese la nota 02: "))
nota03 = int(input("Ingrese la nota 03: "))

promedio = (nota01 + nota02 + nota03) / 3 

if(promedio>=6):
    print("Aprobado. Nota:", round(promedio, 2))
else:
    print("En suspenso. Nota: ", round(promedio, 2))

