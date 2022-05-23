
import random

def FO(datos):
    i = 0
    return sum(datos)

datos = []
n=0
while n<2:
    n = int(input("Ingrese el tamaño del arreglo\n"))
    if n<2:
        print("El tamaño del arreglo debe ser mayor o igual a 2")

for _ in range(n):
    datos.append(random.randint(0,1))
valor= FO(datos)
print ("El resultado de la suma es: "+str(valor))

