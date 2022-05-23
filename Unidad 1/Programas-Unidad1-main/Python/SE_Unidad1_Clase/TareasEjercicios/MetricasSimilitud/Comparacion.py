
import Similitud
import random
aleatorio = []

print("Dame un vector de 10 datos (0 y 1)")
valor = input()
entrada = list(map(int, valor.split()))

for i in range(10):
    aleatorio.append(random.randint(0,1))

print("\nSimilitud Manhatan")
print(Similitud.Manhattan(entrada, aleatorio))

print("\nSimilitud Euclidiana")
print(Similitud.Euclidiana(entrada, aleatorio))

print("\nSimilitud Euclidiana Promedio")
print(Similitud.EuclidianaProm(entrada, aleatorio))

print("\nSimilitud Diferencia de Carácter Promedio")
print(Similitud.Diferencia(entrada, aleatorio))

print("\nSimilitud Canberra")
print(Similitud.Canberra(entrada, aleatorio))


