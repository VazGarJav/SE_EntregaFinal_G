def calc_FO(indv):
    return sum(indv)

#m = numero de genes
tot_genes = 10

#n  = numero de vectores
tot_individuos = 100  #numero de individuos

#Poblacion Inicial
import random as rnd
poblacion = []
for i in range(tot_individuos):
    vector = [ rnd.randint(0,1)  for i in range(tot_genes)]
    ##               vector , FO
    poblacion.append([vector, calc_FO(vector)])

#print("Poblacion Inicial: ")
#for indv in poblacion:
#    print(indv)

padres = []
tot_padres = 50

poblacion.sort(key= lambda x:x[1], reverse=True)
#sorted(poblacion, key= lambda)

print("Poblacion Ordenada: ")
for indv in poblacion:
    print(indv)

#Me quedo con los MejoresPadres
#poblacion = poblacion[0:tot_padres]
#print("tot poblaciond de mejores: " , len(poblacion))

for i in range(tot_padres):
    indexPadre1 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
    indexPadre2 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
    while(indexPadre1==indexPadre2):
        indexPadre2 = rnd.randint(0, tot_padres - 1)  # aleatorio entre 0 y n-1

    tempPadre1 = poblacion[indexPadre1][0]
    tempPadre2 = poblacion[indexPadre2][0]

    if calc_FO(tempPadre1) >= calc_FO(tempPadre2):
        padres.append(tempPadre1.copy())
    else:
        padres.append(tempPadre2.copy())

#print("Padres para cruza: ")
#for index, padre in enumerate(padres):
#    print(index,".-", padre)

hijos = []
for i in range(0,tot_padres, 2):
    tempPadre1 = padres[i]
    tempPadre2 = padres[i+1]

    #Generar un aleatorio
    puntoCruza = rnd.randint(0, tot_genes-1)

    #La primera parte del padre 1, será la primera parte del hijo 1,
    # la segunda parte del padre 1, será la segunda parte del hijo 2

    # La primera parte del padre 2, será la primera parte del hijo 2,
    # la segunda parte del padre 2, será la segunda parte del hijo 1

    # Generar un aleatorio
    puntoCruza += 1  # +1 -> puntoCruza incluyente
    hijo1 = tempPadre1[:puntoCruza] + tempPadre2[puntoCruza:]
    hijo2 = tempPadre2[:puntoCruza] + tempPadre1[puntoCruza:]

    hijos.append([hijo1, 0])
    hijos.append([hijo2, 0])


#Mutacion
probMuta = 0.8
for indexHijo in range(len(hijos)):
    hijo = hijos[indexHijo][0]

    for indexGen in range(len(hijo)):
        r = rnd.random() # 0 - 1
        if r >= probMuta:
            #se efectua la mutacion
            val = 1 if rnd.random() >= 0.5 else 0
            #print(val)
            hijo[indexGen] = val

    hijos[indexHijo][1] = calc_FO(hijo)

##poblacion completa
#hijos