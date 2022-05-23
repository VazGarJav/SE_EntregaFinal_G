
import serial as s
arduino = s.Serial('COM3', baudrate=9600, timeout=1)

import time as t

from pynput.keyboard import Key, Controller
teclado = Controller()

while True:
    val = arduino.readline().decode()
    val = val.replace("\n","")
    val = val.replace("\r", "")
    print(val)

    if val == '1':
        teclado.press('a')
        teclado.release('a')
    else:
        pass
        #no se hace nada

    t.sleep(.1)

