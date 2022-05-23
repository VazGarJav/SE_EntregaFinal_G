
from pynput.keyboard import Key, Controller

teclado = Controller()

teclado.press('u')
teclado.press('a')
teclado.press('t')

teclado.release('u')
teclado.release('a')
teclado.release('t')

teclado.type('\nuat')



