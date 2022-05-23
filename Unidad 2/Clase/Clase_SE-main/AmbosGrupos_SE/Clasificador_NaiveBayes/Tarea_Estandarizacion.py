import numpy as n


#############################################
### Vazquez Garcia Javier Margarito
### Borjas Mercado Luis Enrique


###CARGAR INSTANCIA
archivo = open("Estandarizacion_iris.txt")  #ABRE EL ARCHIVO
contenido = archivo.readlines()  #LEE TODO EL CONTENIDO DEL ARCHIVO
#############################################################################################
lista = [linea.split("\t") for linea in contenido]
instancia = [list(map(int,i)) for i in lista ]

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print("\n")
print("Instancia Procesada: ")
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n")
########################### Promedio y estandarizacion #########################
nor=[]
des=[]
est=[]
prom=[]
for i in range(len(instancia)):
    renglon=[]
    for j in range(len(instancia[0])):
        renglon.append((instancia[i][j]))
    nor.append(renglon)


nor = n.array(nor)
nor = nor.T
des = nor
est = nor
prom = nor
prom = n.mean(nor, axis=0)
des = n.std(des, axis=0)

est=[]

for i in range (nor.shape[1]):
    desv=n.std(nor[:,i])
    prom=n.mean(nor[:,i])
    columna=[]
    for j in range (nor.shape[0]):
        columna.append((nor[j][i]-prom)/desv)
    est.append(columna)

est = n.array(est)
est = est.T
print("Promedio")
print(prom)
print("\n")
print("Desviacion estandar")
print(des)
print("\n")
print("Estandarizacion")
for i in range(est.shape[0]):
    print(str(i+1) +" "+ str(est[i]))


