def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia

###CARGAR INSTANCIA DE ENTRENAMIENTO

archivo = open("iris_entrenamiento.csv","r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")


instancia = [ [ list(map(float,x[:4])), x[4] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(instancia))

print("Instancia de entrenamiento:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")


##############################################################################
###CARGAR INSTANCIA DE PRUEBA

archivo = open("iris_prueba.csv","r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")

prueba = [ [ list(map(float,x[:4])), x[4] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(prueba))

print("Instancia de prueba:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in prueba:
    print(l)
print("\n\n")

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
K = 2
##############################################################################

contAciertos = 0 #contador de aciertos obtenidos en la clasificación 

for registroNC in prueba: #para recorrer a todos los registros de prueba y aplicar al algoritmo K-NN
    print("Clasificación del registro: ")
    print(registroNC) #registor de prueba procesado para su clasificacion

    NC = registroNC[0] #vector de caracteristicas del registro actual de prueba

    estructuraDatos = {} #inicializacion de la estructura de datos

    for NoCaso, i in enumerate(instancia):
        distancia_NC_i = Euclidiana(NC, i[0])
        #print(distancia_NC_i)
        estructuraDatos[NoCaso] = distancia_NC_i

    #print(estructuraDatos)  # La distancia de los registros con el registroNC

    ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1]) #ordena los registros
    #de menor a mayor de acuerdo con la distancia con el registroNC
    #print(ordenado)

    temporalK = []
    for i in range(K):
        NoCaso = ordenado[i][0]
        #print(etiqueta)
        registro = instancia[NoCaso]
        #print(registro)
        temporalK.append(registro[1]) #obtencion de la etiqueta

    print("Clases de los vectores más cercanos al registro NC:")
    print(temporalK)  #los primeros K vectores
    print("\n\n")


    from statistics import multimode  #<<<- realizado unicamente para fines academicos, no se recomienda poner la importacion aqui 
    moda = multimode(temporalK)    
    respKnn = moda[0]  # si existe más de una moda se queda con la primera de ellas  

    print("Clase asignada por el KNN: "  + str(respKnn))
    print("Clase Real: " + registroNC[1])

    if str(respKnn) == registroNC[1]:
        contAciertos += 1

print("Total de aciertos: " + str(contAciertos))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(contAciertos/len(prueba)*100))

#Practica:
#Realizar la aplicación de KNN para el calculo del rendimiento de la técnica utilizando la instancia WINE
#   Consideraciones:
#           *Añadir el código necesario para realizar la busqueda automatizada del valor de K que de mejores resultados
#           *Reportar que valor de K es el mejor y que rendimiento genera
#           *PROBAR OTRAS METRICAS DE SIMILITUD
#           *Generar matriz de confusión

