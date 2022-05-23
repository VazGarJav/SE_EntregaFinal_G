
import serial as conector

arduino = conector.Serial("COM3",baudrate=9600, timeout=1)

valor = arduino.readline()

print(valor)