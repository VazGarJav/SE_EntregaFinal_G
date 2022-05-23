import serial as connector #para conectar con Arduino

import sys

import serial as s

from pynput.keyboard import Key, Controller

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog15.ui"  # Nombre del archivo aquí.

teclado = Controller()

#arduino = s.Serial('COM3', baudrate=9600,timeout=1)

import time as t

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
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

                while True:
                    val = self.arduino.readline().decode()
                    val = val.replace("\n", "")
                    val = val.replace("\r", "")
                    if (val == '1'):
                        self.txt_line.setText(self.txt_line.text()+"A")
                    else:
                        pass
                    t.sleep(0.100)

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

    #def accion(self):
     #   if self.arduino != None:
     #       if self.arduino.isOpen():  ##otra opción: checar que el texto del boton sea desconectar
     #           self.arduino.write("1".encode())
     #           print("El dato ha sido enviado correctamente")
     #       else:
     #           print("La conexión esta cerrada actualmente")
     #   else:
     #       print("Aun no se ha realizado la conexion con Arduino")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())







