import serial as connector #para conectar con Arduino

import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog6.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None #null en java



    # Área de los Slots
    def conectar(self):
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

    def accion(self):
        if self.arduino != None:
            if self.arduino.isOpen():  ##otra opción: checar que el texto del boton sea desconectar
                self.arduino.write("1".encode())
                print("El dato ha sido enviado correctamente")
            else:
                print("La conexión esta cerrada actualmente")
        else:
            print("Aun no se ha realizado la conexion con Arduino")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

