from modelo.persona import Persona

class Supervisor(Persona):
    def __init__(self, nombre, apellido, rut, area):#constructor
        super().__init__(nombre, apellido, rut) #invocando a los atributos de la superclase Persona
        self._area = area #atributo agregado a la clase o sub clase Supervisor

    @property #get()
    def area(self):
        return self._area
    
    @area.setter #set()
    def area(self, area):
        self._area = area
        
    def __str__(self): #funcion para imprimir el objeto en string, en cualquier tipo de estructura
        #return super().__str__()
        return f'supervisor(nombre: {self._nombre}, apellido: {self._apellido}, rut: {self._rut}, area: {self._area})'
    