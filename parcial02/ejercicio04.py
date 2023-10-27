#Calcular el área de un triángulo. Validar que la base y la altura dada por el usuario, sean mayores que 0.
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

if(base > 0 and altura > 0):
    area = (base*altura)/2
    print("El area del triangulo es:", area)
else:
    print("Verifique que la altura y la base sean mayores a 0")
