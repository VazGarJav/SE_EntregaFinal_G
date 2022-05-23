import serial as connector #para conectar con Arduino
import sys
import sender
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Tarea_003.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_config1.clicked.connect(self.accion)
        self.btn_config2.clicked.connect(self.accion)
        self.btn_config3.clicked.connect(self.accion)
        self.btn_config4.clicked.connect(self.accion)
        self.btn_config5.clicked.connect(self.accion)
        self.btn_config6.clicked.connect(self.accion)
        self.btn_config7.clicked.connect(self.accion)
        self.btn_config8.clicked.connect(self.accion)
        self.btn_config9.clicked.connect(self.accion)
        self.btn_config10.clicked.connect(self.accion)
        self.valor = 0
        self.parametro = 0
        self.cadena =""
        self.lista=[]
        self.arduino = None #null en java

    # Área de los Slots
    def conectar(self):
        try:
            if self.arduino == None:
                com = "COM"+ self.txt_com.text()
                self.txt_com.setEnabled(False)
                self.arduino =  connector.Serial(com, baudrate=9600, timeout=1)  #Establece la conexion por primera vez
                print("Conexión Inicializada")
                self.btn_conectar.setText("DESCONECTAR")
            elif self.arduino.isOpen(): ##otra opción: checar que el texto del boton sea desconectar
                self.btn_conectar.setText("RECONECTAR")
                self.arduino.close()
                print("Conexion Cerrada")
            else:
                self.btn_conectar.setText("DESCONECTAR")
                self.arduino.open()
                print("Conexion Reconectada")
        except Exception as e:
            print(str(e))

    def accion(self):
        if self.arduino != None:
            if self.arduino.isOpen():  ##otra opción: checar que el texto del boton sea desconectar
                self.cadena=""
                sender = self.sender().text()
                self.valor = int(self.txt_com.text())
                self.txt_com.setEnabled(False)
                self.parametro= int(sender[7:])-1
                self.leerarchivo()
                self.concatenar()
                self.arduino.write(self.cadena.encode())
                print("El dato ha sido enviado correctamente")
            else:
                print("La conexión esta cerrada actualmente")
        else:
            print("Aun no se ha realizado la conexion con Arduino")

    def leerarchivo(self):
        archivo = open("archivo.csv")
        contenidoArchivo = archivo.readlines()
        #print(contenidoArchivo)
        archivoProcesado = [i.split(",") for i in contenidoArchivo]
        instancia = [list(map(int, i)) for i in archivoProcesado]
        self.lista =  instancia[self.parametro]

    def concatenar(self):
        for i in range(len(self.lista)):
            #print (str(self.lista[i]))
            self.cadena = self.cadena + "" + str(self.lista[i])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
