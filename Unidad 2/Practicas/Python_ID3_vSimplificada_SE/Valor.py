
class Valor:
    
    def __init__(self, nombreAtributo, etiqueta= ""):                     
        self.nombreAtributo = nombreAtributo
        self.etiqueta = etiqueta
    
    def __eq__(self, other): 
        if not isinstance(other, Valor):            
            return NotImplemented
        return self.nombreAtributo == other.nombreAtributo

    def __hash__(self):        
        return hash((self.nombreAtributo))
        
    def __str__(self):
        return self.etiqueta

    def __repr__(self):
        return str(self)