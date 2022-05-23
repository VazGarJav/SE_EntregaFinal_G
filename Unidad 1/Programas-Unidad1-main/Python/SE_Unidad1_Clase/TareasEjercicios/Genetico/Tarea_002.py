
import random
def FO(matriz,n,m):
    i = 0
    suma = 0
    j = 0
    for i in range (m):
        for j in range (n):
            suma+=matriz[i][j]
    print (suma)

datos = []
matriz  = []
n=0
while n<2:
    n = int(input("Ingrese el tamaño del arreglo\n"))
    if n<2:
        print("El tamaño del arreglo debe ser mayor o igual a 2, vuelva a ingresar el tamaño\n")
m=0
while m<1:
    m = int(input("Cuantos arreglos desea crear\n"))
    if m<1:
        print("Al menos se debe crear un arreglo, vuelva a ingresar la cantidad\n")
for _ in range(m):
    for _ in range(n):
        datos.append(random.randint(0,1))
    matriz.append(datos)
    datos=[]
print ("El resultado de la suma es: ")
FO(matriz,n,m)

