from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre, apellido, rut) #invocando a los atributos de la superclase Persona
        self._descuento = descuento

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento
        
    def __str__(self):
        #return super().__str__()
        return f'cliente(nombre: {self._nombre}, apellido: {self._apellido}, rut: {self._rut}, descuento: {self._descuento})'
          