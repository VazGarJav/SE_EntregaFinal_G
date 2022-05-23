from select import select
import P5_AL_EvaluadorInstancias as asolin
import Iris_AL as iris
import Cancer_AL as cancer
import Wine_AL as wine
import Naive_bayes as naive
import KNN_iris as knn
import knn_wine as knn_wine
import knn_clase as knn_clase
import knn_cancer as knn_cancer
import Naive_cancer as naive_cancer
import Naive_wine as naive_wine
import Naive_clase as naive_clase
import serial as connector #para conectar con Arduino
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QVBoxLayout

qtCreatorFile = "Proyect.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.Asocia()
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_aceptar.clicked.connect(self.Asocia)
        self.btn_clear.clicked.connect(self.Limpiar)


        self.arduino = None #null en java

    # Área de los Slots
    def conectar(self):
        try:

            if self.arduino == None:
                com = "COM"+ self.txt_com.text()
                self.txt_com.setEnabled(False)
                self.arduino =  connector.Serial(com, baudrate=9600, timeout=1)
                #Establece la conexion por primera vez
                print("Conexión Inicializada")
                self.plainText.setPlainText("Conexion Inicializada")
                self.btn_conectar.setText("DESCONECTAR")
            elif self.arduino.isOpen(): ##otra opción: checar que el texto del boton sea desconectar
                self.btn_conectar.setText("RECONECTAR")
                self.arduino.close()
                print("Conexion Cerrada")
                self.plainText.setPlainText("Conexion Cerrada")
            else:
                self.btn_conectar.setText("DESCONECTAR")
                self.arduino.open()
                print("Conexion Reconectada")
                self.plainText.setPlainText("Conexion Reconectada")
        except Exception as e:
            print(str(e))

    def accion(self):
        if self.arduino != None:
            if self.arduino.isOpen():  ##otra opción: checar que el texto del boton sea desconectar
                self.arduino.write("1".encode())
                print("El dato ha sido enviado correctamente")
                self.plainText.setPlainText("El dato ha sido enviado correctamente")
            else:
                print("La conexión esta cerrada actualmente")
                self.plainText.setPlainText("La conexión esta cerrada actualmente")
        else:
            print("Aun no se ha realizado la conexion con Arduino")
            self.plainText.setPlainText("Aun no se ha realizado la conexion con Arduino")

    def Asocia(self):
        try:

            if self.arduino != None:
    ################# ASOCIADOR LINEAL ############
                if self.rb_AsoLin.isChecked() and self.rb_cancer.isChecked():
                    self.lb_alg.setText("Asociador Lineal")
                    print(self.rb_AsoLin.text() + " is selected")
                    print("Seleccionaste el asociador lineal")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_AsoLin.text() + " y " + self.rb_cancer.text())
                    self.plainText.appendPlainText("Clase asignada: " + cancer.Clases[asolin.IndexMaxYcasoi])
                    self.plainText.appendPlainText("Clase Real: " + cancer.Clases[asolin.IndexMaxYrealcasoi])
                    self.plainText.appendPlainText("Total de Casos Correctos: " + cancer.casosCorrectos.__str__())
                    self.plainText.appendPlainText("Eficiencia del Asociador Lineal: " + (cancer.casosCorrectos / asolin.X.shape[1] * 100.0).__str__())
                    self.plainText.appendPlainText("Total de Casos Analizados: " + (cancer.X.shape[1]).__str__())

                elif self.rb_AsoLin.isChecked() and self.rb_wine.isChecked():
                    self.lb_alg.setText("Asociador Lineal")
                    print(self.rb_AsoLin.text() + " is selected")
                    print("Seleccionaste el asociador lineal")
                    self.plainText.appendPlainText("Clase asignada: " + wine.Clases[wine.IndexMaxYcasoi])
                    self.plainText.appendPlainText("Clase Real: " + wine.Clases[wine.IndexMaxYrealcasoi])
                    self.plainText.appendPlainText("Total de Casos Correctos: " + wine.casosCorrectos.__str__())
                    self.plainText.appendPlainText(
                        "Eficiencia del Asociador Lineal: " + (wine.casosCorrectos / wine.X.shape[1] * 100.0).__str__())
                    self.plainText.appendPlainText("Total de Casos Analizados: " + (wine.X.shape[1]).__str__())


                elif self.rb_AsoLin.isChecked() and self.rb_clases.isChecked():
                    self.lb_alg.setText("Asociador Lineal")
                    print(self.rb_AsoLin.text() + " is selected")
                    print("Seleccionaste el asociador lineal")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_AsoLin.text() + " y " + self.rb_clases.text())
                    self.plainText.appendPlainText("Clase asignada: " + asolin.Clases[asolin.IndexMaxYcasoi])
                    self.plainText.appendPlainText("Clase Real: " + asolin.Clases[asolin.IndexMaxYrealcasoi])
                    self.plainText.appendPlainText("Total de Casos Correctos: " + asolin.casosCorrectos.__str__())
                    self.plainText.appendPlainText("Eficiencia del Asociador Lineal: " + (asolin.casosCorrectos / asolin.X.shape[1] * 100.0).__str__())
                    self.plainText.appendPlainText("Total de Casos Analizados: " + (asolin.X.shape[1]).__str__())

                elif self.rb_AsoLin.isChecked() and self.rb_iris.isChecked():
                    self.lb_alg.setText("Asociador Lineal")
                    print(self.rb_AsoLin.text() + " is selected")
                    print("Seleccionaste el asociador lineal")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_AsoLin.text() + " y " + self.rb_iris.text())
                    self.plainText.appendPlainText("Clase asignada: " + iris.Clases[asolin.IndexMaxYcasoi])
                    self.plainText.appendPlainText("Clase Real: " + iris.Clases[asolin.IndexMaxYrealcasoi])
                    self.plainText.appendPlainText("Total de Casos Correctos: " + iris.casosCorrectos.__str__())
                    self.plainText.appendPlainText("Eficiencia del Asociador Lineal: " + (iris.casosCorrectos/asolin.X.shape[1]*100.0).__str__())
                    self.plainText.appendPlainText("Total de Casos Analizados: " + (iris.X.shape[1]).__str__())


        ##################### NAIVE BAYES ###################
                elif self.rb_NaiBay.isChecked() and self.rb_cancer.isChecked():
                    self.lb_alg.setText("Naive Bayes")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_NaiBay.text() + " y " + self.rb_cancer.text())
                    print(self.rb_NaiBay.text() + " is selected")
                    print("Seleccionaste el Naive Bayes")
                    print("\n\nCorrect Classify: ", naive_cancer.correct_classify, " Total Evaluated: ", len(naive_cancer.dataset),
                          " Efficiency: ", round(naive_cancer.correct_classify / len(naive_cancer.dataset) * 100, 4), "%")
                    self.plainText.appendPlainText("Correct Classify: " + naive_cancer.correct_classify.__str__() + "%")
                    self.plainText.appendPlainText(" Total Evaluated: " + (len(naive_cancer.dataset)).__str__())
                    self.plainText.appendPlainText(
                        " Efficiency: " + (round(naive_cancer.correct_classify / len(naive_cancer.dataset) * 100, 4)).__str__())

                    print("Real Class: ", naive.dataset[naive_cancer.k][-1], "Assigned Class: ", naive_cancer.c_toAssign,
                          " Probability: ", round(naive_cancer.max * 100, 4), "%")
                    self.plainText.appendPlainText("Real Class: " + (naive_cancer.dataset[naive_cancer.k][-1]).__str__())
                    self.plainText.appendPlainText("Assigned Class: " + naive_cancer.c_toAssign.__str__())
                    self.plainText.appendPlainText(" Probability: " + (round(naive_cancer.max * 100, 4)).__str__() + "%")
                elif self.rb_NaiBay.isChecked() and self.rb_wine.isChecked():
                    self.lb_alg.setText("Naive Bayes")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_NaiBay.text() + " y " + self.rb_wine.text())
                    print(self.rb_NaiBay.text() + " is selected")
                    print("Seleccionaste el Naive Bayes")
                    print("\n\nCorrect Classify: ", naive_wine.correct_classify, " Total Evaluated: ", len(naive_wine.dataset),
                          " Efficiency: ", round(naive_wine.correct_classify / len(naive_wine.dataset) * 100, 4), "%")
                    self.plainText.appendPlainText("Correct Classify: " + naive_wine.correct_classify.__str__() + "%")
                    self.plainText.appendPlainText(" Total Evaluated: " + (len(naive_wine.dataset)).__str__())
                    self.plainText.appendPlainText(
                        " Efficiency: " + (round(naive_wine.correct_classify / len(naive_wine.dataset) * 100, 4)).__str__())

                    print("Real Class: ", naive.dataset[naive_wine.k][-1], "Assigned Class: ", naive_wine.c_toAssign,
                          " Probability: ", round(naive.max * 100, 4), "%")
                    self.plainText.appendPlainText("Real Class: " + (naive_wine.dataset[naive_wine.k][-1]).__str__())
                    self.plainText.appendPlainText("Assigned Class: " + naive_wine.c_toAssign.__str__())
                    self.plainText.appendPlainText(" Probability: " + (round(naive_wine.max * 100, 4)).__str__() + "%")

                elif self.rb_NaiBay.isChecked() and self.rb_clases.isChecked():
                    self.lb_alg.setText("Naive Bayes")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_NaiBay.text() + " y " + self.rb_clases.text())
                    print(self.rb_NaiBay.text() + " is selected")
                    print("Seleccionaste el Naive Bayes")
                    print("\n\nCorrect Classify: ", naive_clase.correct_classify, " Total Evaluated: ", len(naive_clase.dataset),
                          " Efficiency: ", round(naive_clase.correct_classify / len(naive_clase.dataset) * 100, 4), "%")
                    self.plainText.appendPlainText("Correct Classify: " + naive_clase.correct_classify.__str__() + "%")
                    self.plainText.appendPlainText(" Total Evaluated: " + (len(naive_clase.dataset)).__str__())
                    self.plainText.appendPlainText(
                        " Efficiency: " + (round(naive_clase.correct_classify / len(naive_clase.dataset) * 100, 4)).__str__())

                    print("Real Class: ", naive_clase.dataset[naive_clase.k][-1], "Assigned Class: ", naive_clase.c_toAssign,
                          " Probability: ", round(naive_clase.max * 100, 4), "%")
                    self.plainText.appendPlainText("Real Class: " + (naive_clase.dataset[naive_clase.k][-1]).__str__())
                    self.plainText.appendPlainText("Assigned Class: " + naive_clase.c_toAssign.__str__())
                    self.plainText.appendPlainText(" Probability: " + (round(naive_clase.max * 100, 4)).__str__() + "%")

                elif self.rb_NaiBay.isChecked() and self.rb_iris.isChecked():
                    self.lb_alg.setText("Naive Bayes")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_NaiBay.text() + " y " + self.rb_iris.text())
                    print(self.rb_NaiBay.text() + " is selected")
                    print("Seleccionaste el Naive Bayes")
                    print("\n\nCorrect Classify: ", naive.correct_classify, " Total Evaluated: ",len(naive.dataset)," Efficiency: ",round(naive.correct_classify / len(naive.dataset) * 100, 4), "%")
                    self.plainText.appendPlainText("Correct Classify: " + naive.correct_classify.__str__() + "%")
                    self.plainText.appendPlainText(" Total Evaluated: " + (len(naive.dataset)).__str__())
                    self.plainText.appendPlainText(" Efficiency: " + (round(naive.correct_classify / len(naive.dataset) * 100, 4)).__str__())

                    print("Real Class: ", naive.dataset[naive.k][-1], "Assigned Class: ", naive.c_toAssign, " Probability: ",round(naive.max * 100, 4), "%")
                    self.plainText.appendPlainText("Real Class: " + (naive.dataset[naive.k][-1]).__str__())
                    self.plainText.appendPlainText("Assigned Class: " + naive.c_toAssign.__str__())
                    self.plainText.appendPlainText(" Probability: " + (round(naive.max * 100, 4)).__str__() + "%")



                ############## KNN #######################
                elif self.rb_Knn.isChecked() and self.rb_cancer.isChecked():
                    self.lb_alg.setText("KNN")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_Knn.text() + " y " + self.rb_cancer.text())
                    print(self.rb_Knn.text() + " is selected")
                    print("Seleccionaste " + self.rb_Knn.text())
                    self.plainText.appendPlainText("Clase asignada por el KNN: " + (knn_cancer.respKnn).__str__())
                    self.plainText.appendPlainText("Clase Real: " + (knn_cancer.registroNC[1]).__str__())
                    self.plainText.appendPlainText("Total de aciertos: " + str(knn_cancer.contAciertos))
                    self.plainText.appendPlainText("Total de pruebas: " + str(len(knn_cancer.prueba)))
                    self.plainText.appendPlainText("Rendimiento: " + str(knn_cancer.contAciertos / len(knn_cancer.prueba) * 100))
                elif self.rb_Knn.isChecked() and self.rb_wine.isChecked():
                    self.lb_alg.setText("KNN")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_Knn.text() + " y " + self.rb_wine.text())
                    print(self.rb_Knn.text() + " is selected")
                    print("Seleccionaste " + self.rb_Knn.text())
                    self.plainText.appendPlainText("Clase asignada por el KNN: " + (knn_wine.respKnn).__str__())
                    self.plainText.appendPlainText("Clase Real: " + (knn_wine.registroNC[1]).__str__())
                    self.plainText.appendPlainText("Total de aciertos: " + str(knn_wine.contAciertos))
                    self.plainText.appendPlainText("Total de pruebas: " + str(len(knn_wine.prueba)))
                    self.plainText.appendPlainText("Rendimiento: " + str(knn_wine.contAciertos / len(knn_wine.prueba) * 100))
                elif self.rb_Knn.isChecked() and self.rb_clases.isChecked():
                    self.lb_alg.setText("KNN")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_Knn.text() + " y " + self.rb_clases.text())
                    print(self.rb_Knn.text() + " is selected")
                    print("Seleccionaste " + self.rb_Knn.text())
                    self.plainText.appendPlainText("Clase asignada por el KNN: " + (knn_clase.respKnn).__str__())
                    self.plainText.appendPlainText("Clase Real: " + (knn_clase.registroNC[1]).__str__())
                    self.plainText.appendPlainText("Total de aciertos: " + str(knn_clase.contAciertos))
                    self.plainText.appendPlainText("Total de pruebas: " + str(len(knn_clase.prueba)))
                    self.plainText.appendPlainText("Rendimiento: " + str(knn_clase.contAciertos / len(knn_clase.prueba) * 100))
                elif self.rb_Knn.isChecked() and self.rb_iris.isChecked():
                    self.lb_alg.setText("KNN")
                    self.plainText.appendPlainText("Seleccionaste " + self.rb_Knn.text() + " y " + self.rb_iris.text())
                    print(self.rb_Knn.text() + " is selected")
                    print("Seleccionaste " + self.rb_Knn.text())
                    self.plainText.appendPlainText("Clase asignada por el KNN: " + (knn.respKnn).__str__())
                    self.plainText.appendPlainText("Clase Real: " + (knn.registroNC[1]).__str__())
                    self.plainText.appendPlainText("Total de aciertos: " + str(knn.contAciertos))
                    self.plainText.appendPlainText("Total de pruebas: " + str(len(knn.prueba)))
                    self.plainText.appendPlainText("Rendimiento: " + str(knn.contAciertos / len(knn.prueba) * 100))
                   # if(knn.registroNC[1]).__str__() == (knn.respKnn).__str__():
                    #    self.arduino.write("1")
                else:
                    self.lb_alg.setText("Seleccione uno")
                    self.plainText.appendPlainText("Por favor seleccione una de las opciones de instancia y algoritmos")

            else:
                self.plainText.setPlainText("La conexión esta cerrada actualmente")
        except Exception as e:
            print(str(e))
    def Limpiar(self):
        if self.arduino != None:
            self.plainText.setPlainText("")
        else:
            self.plainText.setPlainText("La conexión esta cerrada actualmente")
















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
