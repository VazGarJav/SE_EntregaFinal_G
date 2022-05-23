import numpy as n


#############################################
### Vazquez Garcia Javier Margarito
### Borjas Mercado Luis Enrique


###CARGAR INSTANCIA
archivo = open("Normalizacion_clase.txt")  #ABRE EL ARCHIVO
contenido = archivo.readlines()  #LEE TODO EL CONTENIDO DEL ARCHIVO
#############################################################################################
lista = [linea.split("\t") for linea in contenido]
instancia = [list(map(int,i)) for i in lista ]

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print("Instancia Procesada: ")
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")
########################### MAXIMOS Y MINIMOS #########################
m=[]
mi=[]
nor=[]
mm=[]
cont = 0
for i in range(len(instancia)):
    maximo = max(instancia[i])
    print("maximo: ", maximo)
    minimo = min(instancia[i])
    print("minimo: ", minimo)
    renglon=[]
    for j in range(len(instancia[0])):
        renglon.append((instancia[i][j]-minimo)/(maximo-minimo))
    nor.append(renglon)

nor = n.array(nor)
print("nor n: ")
print(nor)
nor = nor.T
print("nor T: " , nor)
complemento=[]
for i in range(len(instancia)):
    renglon=[]
    for j in range(len(instancia[0])):
        renglon.append(1-nor[j][i])
    complemento.append(renglon)

print("Normalizacion")
print(nor)

print("\nComplemento")
print(complemento)