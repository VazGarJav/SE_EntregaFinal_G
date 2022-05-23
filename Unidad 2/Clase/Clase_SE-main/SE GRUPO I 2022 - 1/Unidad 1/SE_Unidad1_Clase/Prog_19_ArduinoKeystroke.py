
import serial as s
arduino = s.Serial("com3", baudrate=9600, timeout=1)

import time as t

from pynput.keyboard import Key, Controller
teclado = Controller()


while True:
    val = arduino.readline().decode() #\n\r
    val = val.replace("\n","")
    val = val.replace("\r", "")
    print(val)

    if val == "1":
        teclado.press("A")
        teclado.release("A")
    else:
        pass

    t.sleep(.1) #100milisegundos




