import serial as connector #para conectar con Arduino
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "ProyectoU1.ui"

from pynput.keyboard import Key, Controller
teclado = Controller()

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
                self.accion()
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
                while True:
                    val = self.arduino.readline().decode()
                    val = val.replace("\n", "")
                    val = val.replace("\r", "")
                    if (val == '0'):
                        teclado.press(Key.left)
                        teclado.release(Key.left)
                    else:
                        if(val=='1'):
                            teclado.press(Key.down)
                            teclado.release(Key.down)
                        else:
                            if(val=='2'):
                                teclado.press(Key.up)
                                teclado.release(Key.up)
                            else:
                                if(val=='3'):
                                    teclado.press(Key.right)
                                    teclado.release(Key.right)
                    t.sleep(0.100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
