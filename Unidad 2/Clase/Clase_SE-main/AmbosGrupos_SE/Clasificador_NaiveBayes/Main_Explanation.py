

file2read = open("Instancia_Explicacion_Golf.csv")
file_content = file2read.readlines()

#############################################################################################
dataset = []
for i in file_content:
    dataset.append((i.replace("\n","")).split(","))
headers = dataset[0]
del dataset[0] #remove headers from dataset 
#############################################################################################
##count registers per class
#############################################################################################
probabilities = [] #se cuentan los atributos de cada clase
auxiliar = {}
for register_index in range(len(dataset)): #por cada registro nos interesa la lista de atributos
    label = dataset[register_index][-1] #etiqueta
    if label in auxiliar: #si esta la etiqueta se le incrementa uno si no se agrega la etiqueta
        auxiliar[label] += 1
    else:
        auxiliar[label] = 1
probabilities.append(auxiliar)
#############################################################################################
##count registers per attribute
#############################################################################################
#por cada indice del atributo voy a recorrer a todos los registros para recorrer hacia abajo
for attribute_index in range(len(dataset[0])-1): #cuantos registros hay por atributo por cada clase
    auxiliar = {}#se armara una tupla con la etiqueta y la clase
    for register_index in range(len(dataset)): 
        v_label = dataset[register_index][attribute_index] #se asigna un label para cada atributo
        v_class = dataset[register_index][-1] # se asigna la clase
        if (v_label,v_class) in auxiliar: #si la tupla se encuentra en el diccionario
            auxiliar[(v_label,v_class)] += 1 #se le agrega unn al valor que ya tenia
        else:
            auxiliar[(v_label,v_class)] = 1 #si no se creara
            #print(v_label, "  ", v_class)
    probabilities.append(auxiliar)
#############################################################################################
##calculate probabilities per attribute
#############################################################################################
for index in range(1, len(probabilities)):
    for c in probabilities[index]: #per attribute
        #print(probabilities[index][c]) # se obtienen las probabilidades por cada clase
        #print(probabilities[0][c[1]])
        probabilities[index][c] =  probabilities[index][c]/probabilities[0][c[1]]
    #print(probabilities[0][c])
#############################################################################################
##calculate probabilities per class
#############################################################################################
for c in probabilities[0]: #por cada clase de las probabilidades de cero
    probabilities[0][c] = probabilities[0][c]/len(dataset) #cuantos no se tienen y se dividen entre el total de datos
    #print(probabilities[0][c])
#############################################################################################
#############################################################################################
#############################################################################################
## classify a register
#############################################################################################
register = ["Lluvioso", "Ambiente", "Alta", "Débil"]
#register = ["Soleado", "Frío", "Alta", "Fuerte"] #test1
#register = ["Nublado", "Frío", "Normal", "Fuerte"] #test2


sum = 0
probabilities_per_class = {}
for c in probabilities[0]: #per class por cada clase
    #print(c)
    auxiliar = probabilities[0][c] #es el resultado de haber echo todas las multiplicaciones
    for index in range(1, len(probabilities)):
        print(register[index-1]," ", c)
        if  (register[index-1], c) in probabilities[index]: #si existe una probabilidad para ese caso
            auxiliar *= probabilities[index][(register[index-1], c)]#atributo y clase
            #al aux se le mul la probabilidad de dicho caso en cuestion
        else:
            auxiliar = 0 #nullify the product
    sum += auxiliar
    probabilities_per_class[c] = auxiliar 

max = -9999 #cual es el mas grande despues de calcualr la pribabilidad
c_toAssign = ""
for p in probabilities_per_class: #para cada p sera que la probabilidad de ese va a ser igual
    probabilities_per_class[p] = probabilities_per_class[p]/sum #a la probabilidad que tengo entre la sumatoria
    if probabilities_per_class[p] > max:#si la probabiidad es mayor a la que tengo
        max = probabilities_per_class[p]
        c_toAssign = p # clase asignada 
#############################################################################################
#da una seguridad aparente que ccon la informacion que tiene el esta seguro que la clse que debe asignar es un si
print("Assigned Class: ", c_toAssign, " Probability: ", round(max*100,4), "%")

    
