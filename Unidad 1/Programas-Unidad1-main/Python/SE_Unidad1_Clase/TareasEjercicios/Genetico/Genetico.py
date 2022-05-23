
import random

def FO(vector):
    return sum(vector)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matriz  = []
    n=0

    #Generación de la matriz
    while n<2:
        n = int(input("Ingrese el tamaño del arreglo\n"))
        if n<2:
            print("El tamaño del arreglo debe ser mayor o igual a 2, vuelva a ingresar el tamaño\n")
    m=0
    while m<1:
        m = int(input("Cuantos arreglos desea crear\n"))
        if m<1:
            print("Al menos se debe crear un arreglo, vuelva a ingresar la cantidad\n")
    for i in range(m):
        vector = [ random.randint(0,1)  for i in range(n)]
        matriz.append([vector, FO(vector)])

    matriz.sort(key=lambda x: x[1], reverse=True)

    #Torneo Binario
    padre = []
    matrizpadres = []
    hijos = int(input("Cuantos hijos desea generar ?\n"))
    if(hijos%2==1):
        hijos = hijos + 1
    for i in range (hijos):
        indice1=random.randint(0,hijos-1)
        indice2=random.randint(0,hijos-1)
        while(indice1==indice2):
            indice1=random.randint(0,hijos-1)

        #evaluar cual de los dos gana
        suma1 = matriz[indice1][1]
        suma2 = matriz[indice2][1]
        if(suma1>=suma2):
            padre= matriz[indice1]
        else:
            padre=matriz[indice2]
        matrizpadres.append(padre)

    #realización de parejas y creación de hijos
    matrizhijos = []
    slicing = 0
    for i in range (0, hijos, 2):
        slicing = random.randint(0,n-1)
        hijo1= matrizpadres[i][0][0:slicing] + matrizpadres[i+1][0][slicing:n]
        hijo2= matrizpadres[i+1][0][0:n-slicing] + matrizpadres[i][0][n-slicing:n]
        matrizhijos.append([hijo1,0])
        matrizhijos.append([hijo2,0])

    print("Hijos creados")
    #impresion de los hijos generados
    for i in range (len(matrizhijos)):
            print(str(matrizhijos[i])+ " ")

    print("\nHijos mutados")
    for i in range (len(matrizhijos)):
        for j in range (n):
            rnd = random.random()
            if(rnd>=0.8):
                if(random.random()>=0.5):
                    matrizhijos[i][0][j]=1
                else:
                    matrizhijos[i][0][j]=0
        matrizhijos[i][1]=FO(matrizhijos[i][0])

    for i in range (len(matrizhijos)):
            print(str(matrizhijos[i])+ " ")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
