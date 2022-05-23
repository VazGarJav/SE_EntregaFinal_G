
class Nodo:     
    def __init__(self, id_nodo):                     
        self._etiqueta = ""
        self._ramas = {}
        self._atributo = ""
        self._nodoID = id_nodo
    
    def getEtiqueta(self):
        return self._etiqueta
    
    def getAtributo(self):
        return self._atributo

    def getRamas(self):
        return self._ramas

    def setEtiqueta(self, _etiqueta):
        self._etiqueta = _etiqueta
    
    def addRama(self, value, node):
        self._ramas[value] = node 
    
    def setAtributo(self, _atributo):
        self._atributo = _atributo
    
    def __str__(self):
        ramas_temp = ""
        for key, value in self._ramas.items():    
            ramas_temp += key + ":" + str(value) + "    "
        return "Nodo{" + "_etiqueta=" + self._etiqueta + ", _ramas= " + ramas_temp + ", _atributo=" + self._atributo + ", _nodoID=" + str(self._nodoID) + '}'
    