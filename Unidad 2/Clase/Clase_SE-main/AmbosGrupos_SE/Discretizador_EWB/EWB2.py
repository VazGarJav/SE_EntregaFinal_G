archivo = open("breast-cancer-wisconsin.csv")
#archivo = open("wine.csv")
contenido = archivo.readlines()
#############################################################################################
lectura = []
for i in contenido:
    lectura.append(i.split(","))
encabezados = lectura[0]
del lectura[0]

instancia = [ [ list(map(float,x[:len(x)-1])), x[len(x)-1].strip("\n") ] for x in lectura ]

#############################################################################################
###GRUPOS A GENERAR
v_K = 5    # Pagina de referencia comparativa ->>>>  https://orange.readthedocs.io/en/latest/reference/rst/Orange.feature.discretization.html#Orange.feature.discretization.Discretization
#############################################################################################
intervalos = []

matriz = []
intervalo = []
for index_atributo in range(len(instancia[0][0])):
    auxiliar = []
    for index_registro in range(len(instancia)):
        auxiliar.append(instancia[index_registro][0][index_atributo])
    v_max = max(auxiliar)
    v_min = min(auxiliar)
    v_width = round((v_max-v_min)/v_K,4)

    aux=[]
    valores=[]
    intervalo = []
    control  = round(v_min+v_width,4)
    intervalo.append(control)
    for j in range(1,v_K-1):
        intervalo.append(control)
        control = round(control+v_width,4)
        intervalo.append(control)
    intervalo.append(control)
    intervalos.append(intervalo)
    auxiliar.clear()
#############################################################################################
salida = open("generadocancer.csv", "w")

presalida = []

for j in range(len(instancia[0][0])):
    cadenas = []
    for i in range(len(instancia)):
        cont=1;
        if(instancia[i][0][j]<intervalos[j][0]):
            var = "V"+str(cont)
        else:
            cont = cont + 1
            for k in range(1,len(intervalos[j])-1,2):
                if(instancia[i][0][j]>=intervalos[j][k] and instancia[i][0][j]<intervalos[j][k+1]):
                    var="V"+str(cont)
                cont = cont +1
            if (instancia[i][0][j] >= intervalos[j][len(intervalos[j])-1]):
                var = "V" + str(cont)
        cadenas.append(var)
    presalida.append(cadenas)

auxsalida=[]

for i in range(len(presalida[0])):
    aux2 = []
    for j in range(len(presalida)):
        aux2.append(presalida[j][i])
    auxsalida.append(aux2)

for i in range(len(auxsalida)):
    linea = ""
    for j in range(len(auxsalida[0])):
       linea = linea + auxsalida[i][j] + ","
    linea = linea + str(instancia[i][1]) + "\n"
    salida.write(linea)

salida.close()