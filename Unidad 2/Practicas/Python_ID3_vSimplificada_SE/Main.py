###ESTA ES UNA VERSIÓN SIMPLIFICADA DEL ARBOL INDUCTIVO DE DECISION ID3. 
### 
# NO SE REALIZA LA IMPRESIÓN DEL ÁRBOL. NO OBSTANTE PERMITE LA EVALUACIÓN DE CASOS DE MANERA AUTOMATIZADA
# 
# VERSIÓN ELABORADA EL 30 DE MARZO DE 2022
# DR. ALEJANDRO H. GARCÍA RUIZ
### 
import Valor
import Atributo
import Nodo
import math
contadorNodos = 0
####################################################################################################
def generarVector(listaAtributos, vector):    #Vector = registro/caso/fila
    aux = [];
    for i in range(len(vector)):
        aux.append(Valor.Valor(listaAtributos[i].nombre, vector[i]))    
    return aux
####################################################################################################
def Log2(n):    #version generalizada.. sin embargo, math cuenta con log2
        return math.log10(n) / math.log10(2)
####################################################################################################
def cuantosPorClase(caso, clase):
        total = 0;
        for i in range(len(caso)): # por cada caso            
            if caso[i][len(caso[i]) - 1].etiqueta==clase:
                total+=1                    
        return total
####################################################################################################
def obtenerMejorAtrib(listaAtributos):
    maxGanancia = -99999
    IndiceMax = 0 # si la ganacia es 0, entonces se escoge el primer nodo de forma arbitraria, puede mejorarse
    etropiaAtributo = 0;
    inter = 0;    
    # Etropia del conjunto / arbol
    totalCasos = listaAtributos[len(listaAtributos) - 1].totalCasos    
    etropiaArbol = 0
    for i in range(len(listaAtributos[len(listaAtributos) - 1].listaEtiquetas)):    
        aux = len(listaAtributos[len(listaAtributos) - 1].listaCasos[i]) / totalCasos
        etropiaArbol += -1.0 * aux * Log2(aux)    
    # Etropia del atributo
    for i in range(len(listaAtributos)-1): # por cada atributo
        etropiaAtributo = 0;
        for j in range(len(listaAtributos[i].listaEtiquetas)): # por cada etiqueta
            inter = 0;
            clase = listaAtributos[len(listaAtributos) - 1]
            for k in range(len(clase.listaEtiquetas)): # por cada clase
                aux = cuantosPorClase(listaAtributos[i].listaCasos[j], clase.listaEtiquetas[k])
                if (aux != 0):
                    aux /= len(listaAtributos[i].listaCasos[j]);
                    inter += -1.0 * aux * Log2(aux);                        
            etropiaAtributo += len(listaAtributos[i].listaCasos[j]) / listaAtributos[i].totalCasos * inter;        
        # Ganancia:
        Ganancia = (etropiaArbol - etropiaAtributo) / etropiaArbol;
        # ACTUALIZA aL ATRIBUTO SELECCIONADO...
        if (maxGanancia < Ganancia):
            maxGanancia = Ganancia
            IndiceMax = i        
    return listaAtributos[IndiceMax]
####################################################################################################
def claseMayoritaria(listaCasos, listaEtiquetas):
    claseMayor = ""
    contadores = [0 for i in range(len(listaEtiquetas))]
    indice = -1
    for i in range(len(listaCasos)):
        for j in range(len(listaCasos[i])):            
            indice = listaEtiquetas.index(listaCasos[i][j][len(listaCasos[i][j]) - 1].etiqueta)            
            if (indice != -1):
                contadores[indice]+=1            
    max = -9999;
    for i in range(len(contadores)):
        if (max < contadores[i]):
            max = contadores[i]
            claseMayor = listaEtiquetas[i]        
    return claseMayor;
####################################################################################################
def removerAtributo(caso, nombre):
    indiceColumna = -1    
    for j in range(len(caso)): # Por cada caso        
        if Valor.Valor(nombre) in caso[j]:
            indiceColumna = caso[j].index(Valor.Valor(nombre))
            del caso[j][indiceColumna]                
    return caso;
####################################################################################################
def ID3(casos, listaAtributos, mayoritaria):
    global contadorNodos
    contadorNodos+=1
    root = Nodo.Nodo(contadorNodos)
    mismaClase = False
    aux = -1
    clase = listaAtributos[len(listaAtributos) - 1];
    for k in range(len(clase.listaEtiquetas)): # por cada clase
        aux = cuantosPorClase(casos, clase.listaEtiquetas[k])
        if (aux == len(casos)): # Todos los atributos son de la misma clase            
            mismaClase = True
            root.setEtiqueta(clase.listaEtiquetas[k]);        
    if (not mismaClase):
        if (len(casos)==0):
            root.setEtiqueta(mayoritaria)
        else:
            # PROCESO DE LIMPIA DE LA LISTA DE CASOS DE CADA ETIQUETA
            for i in range(len(listaAtributos)): # Por cada atributo
                for j in range(len(listaAtributos[i].listaEtiquetas)): # por cada etiqueta
                    listaAtributos[i].listaCasos[j] =  []                 
                listaAtributos[i].totalCasos = 0;                                    
            # Generar Lista de Atributos            
            indice=-1            
            for i in range(len(casos)): 
                for j in range(len(listaAtributos)): # por cada atributo.. El ultimo atributo es la clase...
                    indice = listaAtributos[j].listaEtiquetas.index(casos[i][j].etiqueta)
                    listaAtributos[j].listaCasos[indice].append(casos[i])
                    listaAtributos[j].totalCasos+=1                                                    
            A = obtenerMejorAtrib(listaAtributos)            
            root.setAtributo(A.nombre)
            # ELIMINA ATRIBUTO
            for i in range(len(listaAtributos)):
                if listaAtributos[i].nombre == A.nombre:
                    del listaAtributos[i]
                    break
            ##CONTINUA PROCEDIMIENTO                            
            for i in range(len(A.listaEtiquetas)): # Para cada etiqueta (v) del atributo hacer                
                if (len(A.listaCasos)==0):
                    root.setEtiqueta(mayoritaria);
                else:
                    mayoritaria = claseMayoritaria(A.listaCasos, listaAtributos[len(listaAtributos) - 1].listaEtiquetas)
                    A.listaCasos[i]= removerAtributo(A.listaCasos[i], A.nombre)
                    listaAtribsAuxiliar = []
                    listaAtribsAuxiliar.extend(listaAtributos)
                    # Solo se enviarán los casos de la etiqueta en particular...
                    root.addRama(A.listaEtiquetas[i], ID3(A.listaCasos[i], listaAtribsAuxiliar, mayoritaria))    
    return root;
####################################################################################################
def generarVectorToEval(listaAtributos, vector):
    aux = [] 
    for i in range(len(vector)):                                
        aux.append(Valor.Valor(listaAtributos[i].nombre, vector[i]))            
    return aux
####################################################################################################
#EJECUCIÓN PRINCIPAL
archivo = open("cancer_training.csv")
contenido = archivo.readlines()    
##############QUITA \n
for i in range(len(contenido)):
    contenido[i] = contenido[i].replace("\n","")
##############
listaAtributos = []
aux = contenido[0].split(",")
#Lee el nombre de los atributos
for i in range(len(aux)):
    listaAtributos.append(Atributo.Atributo(aux[i]))
#Para Evaluar nuevos casos...
nombresAtributos = []
nombresAtributos.extend(listaAtributos)
##########################################      
for l in range(1, len(contenido)):
    linea = contenido[l]
    aux = linea.split(",")
    #Nota por cada atributo.. El ultimo atributo es la clase...
    for i in range(len(aux)):        
        # añade el caso a la etiqueta correspondiente        
        temporal = generarVector(listaAtributos, aux);
        #////////////////////
        if (aux[i] not in listaAtributos[i].listaEtiquetas):            
            # se añade la etiqueta y el caso al final
            listaAtributos[i].listaEtiquetas.append(aux[i])
            listaAtributos[i].listaCasos.append([])
            # representa por cada etiqueta al valor que le sigue.. ya sea un atributo o una clase
            #listaAtributos[i].siguiente.append(None)         
        indice = listaAtributos[i].listaEtiquetas.index(aux[i])
        listaAtributos[i].listaCasos[indice].append(temporal)
        listaAtributos[i].totalCasos+=1
####################################################################################################
####################################################################################################
# COMIENZA ENTRENAMIENTO (GENERACION) DEL ARBOL ID3
####################################################################################################
####################################################################################################
raiz = obtenerMejorAtrib(listaAtributos) # Sea Raiz el MEJOR de los atributos
####################################################################################################
# ELIMINA ATRIBUTO
for i in range(len(listaAtributos)):
    if listaAtributos[i].nombre == raiz.nombre:
        del listaAtributos[i]
        break
listaAtribsAuxiliar = [] 
####################################################################################################
contadorNodos = 0;
arbol = Nodo.Nodo(contadorNodos)
arbol.setAtributo(raiz.nombre)
r = None;
indiceColumna = -1;
for i in range(len(raiz.listaEtiquetas)): # Para cada etiqueta (v) del atributo hacer    
    contadorNodos+=1
    nodo = Nodo.Nodo(contadorNodos)
    arbol.addRama(raiz.listaEtiquetas[i], nodo)
    #Sea Ejemplos(v) el subconjunto de ejemplos cuyo valor de atributo Raiz es v
    # --- Lista de Casos
    if (len(raiz.listaCasos)==0):
        pass
    else:
        #Sino Devolver Id3(Ejemplos(v), Atributo-objetivo, Atributos/{A})
        mayoritaria = claseMayoritaria(raiz.listaCasos, listaAtributos[len(listaAtributos) - 1].listaEtiquetas);
        raiz.listaCasos[i]= removerAtributo(raiz.listaCasos[i], raiz.nombre);
        listaAtribsAuxiliar = []
        listaAtribsAuxiliar.extend(listaAtributos) 
        #Solo se enviarán los casos de la etiqueta en particular...
        arbol.addRama(raiz.listaEtiquetas[i], ID3(raiz.listaCasos[i], listaAtribsAuxiliar, mayoritaria));
print("Fin Creacion del Arbol")
####################################################################################################
####################################################################################################
# COMIENZA EVALUACIÓN DEL ARBOL ID3
####################################################################################################
####################################################################################################
print("\n\n Evaluación de Casos: ...")
casos = []
try:        
    arch = open("cancer_test.csv")    
    contenido = arch.readlines()    
    ##############QUITA \n
    for i in range(len(contenido)):
        contenido[i] = contenido[i].replace("\n","")
    ##############
    for linea in contenido:
        casos.append(linea.split(","))
except Exception as ex:
    print("Error")

totalCorrectos = 0;
for k in range(len(casos)): #Por cada caso    
    toEvaluar = generarVectorToEval(nombresAtributos, casos[k]);
    temp = arbol
    while (temp.getEtiqueta()==""):
        for i in range(len(toEvaluar)): 
            if temp.getAtributo() == toEvaluar[i].nombreAtributo:
                temp = temp.getRamas()[toEvaluar[i].etiqueta]                    
    claseReal = casos[k][len(casos[k]) - 1]
    print("Clase Asignada: " + temp.getEtiqueta() + " Clase Real: " + claseReal + " Evaluacion: " + str(claseReal == temp.getEtiqueta()));
    if claseReal == temp.getEtiqueta():
        totalCorrectos+=1
    
print("\nRendimiento : " + str(round(totalCorrectos / len(casos) * 100.0,4)));

