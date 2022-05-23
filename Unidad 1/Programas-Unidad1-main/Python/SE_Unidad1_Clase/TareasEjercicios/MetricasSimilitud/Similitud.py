
import math
def Manhattan(A,B):
    suma=0
    for i in range (len(A)):
        suma+=abs(A[i]-B[i])
    return suma

def Euclidiana(A,B):
    suma=0
    for i in range (len(A)):
        suma+= (A[i]-B[i])^2
    suma = math.sqrt(suma)
    return suma

def EuclidianaProm(A,B):
    suma=0
    for i in range (len(A)):
        suma += (A[i] - B[i])^2
    suma=suma/len(A)
    suma=math.sqrt(suma)
    return suma

def Diferencia(A,B):
    suma=0
    for i in range (len(A)):
        suma += abs(A[i] - B[i])
    suma=suma/len(A)
    return suma

def Canberra (A,B):
    suma=0
    for i in range (len(A)):
        try:
            suma+=abs(A[i]-B[i])/((A[i])+(B[i]))
        except:
            suma+=0
    return suma



