class Accesadores:
    def __init__(self):
        self.variable_publico = "puede ser accedido en toda la estructura"
        self._atributo_protected = "puede ser accedido desde fuera de esta clase y desde las subclases"
        self.__atributo_privado = "puede ser accedido solo en la clase declarada"
        
    def get_variable_privada(self):
        return self.__atributo_privado
    
    def set_variable_privada(self,__atributo_privado):
        self.__atributo_privado = __atributo_privado
    
objeto = Accesadores()

print(objeto.get_variable_privada())

print(objeto._atributo_protected)

#dar nuevo valor al atributo privado
objeto.set_variable_privada("nuevo valor")
print(objeto.get_variable_privada())

