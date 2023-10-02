#Programa un bucle que haga una cuenta atrás de 10 hasta 1 y por último escriba el mensaje ‘¡Despegue!’.

from time import sleep

i=10
while (i > 0):
    print(i)
    sleep(0.50)
    i = i - 1
print("¡Despegue!")