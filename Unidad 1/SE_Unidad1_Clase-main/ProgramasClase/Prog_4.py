
import serial as conector
import time
arduino = conector.Serial('COM3',9600)
time.sleep(3)

arduino.write()

t = arduino.readline()

print(t)
