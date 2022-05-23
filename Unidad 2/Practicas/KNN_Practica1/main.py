def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia
def Diferencia(A,B):
    distancia=0
    for i in range (len(A)):
        distancia += abs((A[i] - B[i]))
    distancia=round(distancia/len(A), 2)
    return distancia
def Canberra (A,B):
    distancia=0
    for i in range (len(A)):
        distancia+=(abs(A[i]-B[i]))/abs((A[i]+B[i]))
    return round(distancia, 2)
def Manhattan(A,B):
    distancia=0
    for i in range (len(A)):
        distancia+=abs(A[i]-B[i])
    return distancia
def Coseno(A,B):
    distancia = 0
    arriba = 0
    abajox = 0
    abajoy = 0
    for i in range(len(A)):
        arriba += A[i] + B[i]
        abajox += A[i] ** 2
        abajoy  += B[i] ** 2
    distancia = arriba/((abajox * abajoy) ** (1/2))
    return round(distancia, 2)

###CARGAR INSTANCIA DE ENTRENAMIENTO

archivo = open("wine_training90.0.csv","r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")

#CREA UNA LISTA EN LA QUE CADA ELEMENTO SEA UNA LINEA DEL ARCHIVO CONVERTIDA EN LISTA SEPARADA POR TABULADOR
lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")

#CONVIERTE LA LISTA DE LISTAS EN LA INSTANCIA NECESARIA PARA TRABAJAR CON EL KNN
instancia = [ [ list(map(float,x[:13])), x[13] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(instancia))

print("Instancia de entrenamiento:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")


##############################################################################
###CARGAR INSTANCIA DE PRUEBA

archivo = open("wine_test90.0.csv","r") #ABRE EL ARCHIVO
contenido = archivo.readlines() #LEE TOFO EL CONTENIDO DEL ARCHIVO

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")

#CREA UNA LISTA EN LA QUE CADA ELEMENTO SEA UNA LINEA DEL ARCHIVO CONVERTIDA EN LISTA SEPARADA POR COMA
lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")

#CONVIERTE LA LISTA DE LISTAS EN LA PRUEBA NECESARIA PARA TRABAJAR CON EL KNN
prueba = [ [ list(map(float,x[:13])), x[13] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(prueba))

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print("Instancia de prueba:")
#Impreso línea a línea
for l in prueba:
    print(l)
print("\n\n")

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
contAciertos = 0
aux = 0
cantK = 0
cantAci = 0
for K in range(1, int(len(instancia)/2)):
    contAciertos=0
    for registroNC in prueba:  # para recorrer a todos los registros de prueba y aplicar al algoritmo K-NN
        print("Clasificación del registro: ")
        print(registroNC)  # registor de prueba procesado para su clasificacion

        NC = registroNC[0]  # vector de caracteristicas del registro actual de prueba

        estructuraDatos = {}  # inicializacion de la estructura de datos

        for NoCaso, i in enumerate(instancia): #por cada elemento/registro de la instancia
            distancia_NC_i = Canberra(NC, i[0]) #registro[0] = vector carac   -- registro[1] = clase
            # print(distancia_NC_i)
            estructuraDatos[NoCaso] = distancia_NC_i

        # print(estructuraDatos)  # La distancia de los registros con el registroNC

        ## 0 = NoCaso   1 = Distancia  -->> #retorna una lista de tuplas
        ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1]) #reverse=True  # ordena los registros
        # de menor a mayor de acuerdo con la distancia con el registroNC
        # print(ordenado)

        temporalK = []
        for i in range(K):
            NoCaso = ordenado[i][0] ##0 = NumDeCaso
            # print(etiqueta)
            # registro correspondiente al indice (NoCaso) consultado
            registro = instancia[NoCaso]
            # print(registro)
            temporalK.append(registro[1])  # obtencion de la etiqueta

        print("Clases de los vectores más cercanos al registro NC:")
        print(temporalK)  # los primeros K vectores
        print("\n\n")

        from statistics import \
            multimode  # <<<- realizado unicamente para fines academicos, no se recomienda poner la importacion aqui

        moda = multimode(temporalK)
        respKnn = moda[0]  # si existe más de una moda se queda con la primera de ellas

        print("Clase asignada por el KNN: " + str(respKnn))
        print("Clase Real: " + registroNC[1])

        if str(respKnn) == registroNC[1]:
            contAciertos += 1

    rendimiento = contAciertos / len(prueba) * 100

    if  rendimiento >= aux:
        aux = rendimiento
        cantK = K
        cantAci = contAciertos

print("La mejor K: " + str(cantK))
print("Total de aciertos: " + str(cantAci))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(aux))

#K = 3
##############################################################################

#contAciertos = 0 #contador de aciertos obtenidos en la clasificación




#Practica:
#Realizar la aplicación de KNN para el calculo del rendimiento de la técnica utilizando la instancia WINE
#   Consideraciones:
#           *Añadir el código necesario para realizar la busqueda automatizada del valor de K que de mejores resultados
#           *Reportar que valor de K es el mejor y que rendimiento genera
#           *PROBAR OTRAS METRICAS DE SIMILITUD, minimo 3
#           *Generar matriz de confusión, esta es opcional
#           *checara el codigo y lo que saque de validacion sera la calificacion


