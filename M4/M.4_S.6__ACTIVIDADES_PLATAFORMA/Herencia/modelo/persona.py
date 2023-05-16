class Persona:
    #constructor con parametros para instanciar un objeto de tipo persona
    def __init__(self, nombre, apellido, rut):
        self._nombre = nombre
        self._apellido = apellido
        self._rut = rut
        
    #getters y setters ((saber que pythonyc es la estructura real de python))
    @property #variacion de get() que en su caso sería: get_nombre(self): return self._nombre
    def nombre(self):
        return self._nombre
    
    @nombre.setter #set()
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property #get()
    def apellido(self):
        return self._apellido
    
    @apellido.setter #set()
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property #get()
    def rut(self):
        return self._rut
    
    @rut.setter #set()
    def rut(self, rut):
        self._rut = rut

#########################################
#ejemplos pruebas:
# obj = Persona("fulano", "perez","1-9")
# print(obj.apellido)
#########################################

    #function o method
    def get_tipo(self):
        print(f'soy del tipo {self}')
        print(type(self))
    
    #function para imprimir el objeto en string
    def __str__(self):
        return f'Persona(nombre: {self._nombre}, apellido: {self._apellido}, rut: {self._rut}'
    
    