
import serial as s

from pynput.keyboard import Key, Controller
teclado = Controller()

arduino = s.Serial('COM3', baudrate=9600,timeout=1)

import time as t

while True:
    val=arduino.readline().decode()
    val=val.replace("\n","")
    val=val.replace("\r","")
    print(val)
    if(val =='1'):
        teclado.press('A')
        teclado.release('A')
    else:
        pass
    t.sleep(0.100)
