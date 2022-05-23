
def checkPar(n):
    if n%2==0:
        print("par")
        return 1 #"par"
    else:
        print("impar")
        return 0 #"impar"

lista = [10, 15, 20, 45]
lista = list(map(checkPar, lista))
print(lista)

print("Total de Pares: ", sum(lista))

#for i in lista:
#    checkPar(i)

#for i in lista:
#    if i%2==0:
#        print("par")
#    else:
#        print("impar")

