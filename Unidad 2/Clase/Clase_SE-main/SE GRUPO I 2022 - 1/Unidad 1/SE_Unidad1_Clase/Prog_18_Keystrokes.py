
from pynput.keyboard import Key, Controller

teclado = Controller()

teclado.press('U')
teclado.press('A')
teclado.press('T')

teclado.release('T')
teclado.release('A')
teclado.release('U')

teclado.type('\nUAT')

teclado.press('R')

UAT
UATR