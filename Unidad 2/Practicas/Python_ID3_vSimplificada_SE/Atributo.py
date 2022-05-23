
class Atributo:
    def __init__(self, n):                
        self.nombre = n
        self.listaEtiquetas = []
        self.listaCasos = []
        self.siguiente = [] #Puede ser el nombre de un atributo, o de una clase
        self.totalCasos = 0
        self.esHoja = False

    def agregarEtiqueta(self, etiqueta):
        self.listaEtiquetas.append(etiqueta)
        self.listaCasos.append([]) # Agrego una lista de casos vacia para cada etiqueta

    def agregarCaso(self,etiqueta,caso): #ArrayList<Valor> caso
        indice = self.listaEtiquetas.index(etiqueta)
        self.listaCasos[indice].append(caso)
    
    def __str__(self):
        return self.nombre