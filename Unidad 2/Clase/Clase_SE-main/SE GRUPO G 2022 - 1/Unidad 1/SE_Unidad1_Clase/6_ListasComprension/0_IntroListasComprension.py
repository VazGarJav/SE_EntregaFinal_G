
#CALCULA LA SUMATORIA DE TODOS LOS NUMEROS ENTEROS COMPRENDIDOS ENTRE 1 Y N (Inclusive), Y AÑADELOS A UNA LISTA

# Si n = 8
numeros = [1, 2, 3, 4, 5,6, 7, 8]

#Forma clasica
#n =  int(input("Ingresa el valor de n: "))
#lista = []
#for i in range(1,n+1):
#    lista.append(i)
#print(lista)

#Forma con listas de comprension
n =  int(input("Ingresa el valor de n: "))
lista = [i for i in range(1, n+1)]
print(lista)




