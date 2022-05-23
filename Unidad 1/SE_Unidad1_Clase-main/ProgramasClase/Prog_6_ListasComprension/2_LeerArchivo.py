archivo = open("archivo.csv")  #por defecto es de lectura

contenidoArchivo = archivo.readlines()
print(contenidoArchivo)

archivoProcesado = [i.split(",") for i in contenidoArchivo]
print("archivo procesado: ")
for i in archivoProcesado:
    print(i)

instancia = [list(map(int, i)) for i in archivoProcesado]
print(instancia)

#Tarea: CREAR UNA INTERFAZ GRAFICA QUE LEA A LAS PREFERENCIAS DE LOS USUARIOS, Y CON BASE EN
# UN BOTON CARA CADA USUARIO LES APLIQUE EN ARDUINO.