
from pynput.keyboard import Key, Controller

teclado = Controller()

teclado.press('a')

teclado.release('a')

teclado.type('\nuat')
