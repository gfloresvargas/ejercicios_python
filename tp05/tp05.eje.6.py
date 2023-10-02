#Modificar el código anterior para que los colores del arcoiris aparezcan con las iniciales en mayúscula. Use el método title de str.

colores = ["rojo", "naranja", "amarillo", "verde", "azul", "índigo", "violeta"]
print (colores)
i = 0
for color in colores:
    colores[i] = color.title()
    i = i + 1

print(colores)