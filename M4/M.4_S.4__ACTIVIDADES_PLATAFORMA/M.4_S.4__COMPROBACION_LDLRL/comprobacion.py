# EJERCICIO:
# Codifique en Python una clase que represente a un animal. Un animal tiene las siguientes
# características comunes:
# • Nombre.
# • Raza.
# • Edad.
# • Peso.
# Debe crear dos instancias u objetos de la clase Animal, cuyos objetos son un caballo y un león, con
# las siguientes características particulares:
# Caballo             |   León
# Nombre Zeus         |   Nombre Boulder
# Edad 5 años         |   Edad 10 años
# Raza Pura sangre    |   Raza Atlas
# Peso 450 kg         |   Peso 130 kg

from multipledispatch import dispatch
class Animal:
    #definiendo constructor con parametros
    # def __init__(self,nombre:str,raza:str,edad:int,peso:float):
    #     self.nombre = nombre
    #     self.raza = raza
    #     self.edad = edad
    #     self.peso = peso

  #definiendo constructor con parametros vacíos
    # def __init__(self,nombre = None,raza = None,edad = None,peso = None):
    #     self.nombre = nombre
    #     self.raza = raza
    #     self.edad = edad
    #     self.peso = peso

#con multidispatch para mayor exactitud en el tipo de datos
    @dispatch(str,str,int,float)
    def __init__(self,nombre,raza,edad,peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
  
        
#getter and setters son funciones para obtener o dar valor a los atributos:
#getters
    def get_nombre(self):
        return self.nombre

    def get_raza(self):
        return self.raza
    
    def get_edad(self):
        return self.edad
    
    def get_peso(self):
        return self.peso
 
#setters
    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_raza(self,raza):
        self.raza = raza

    def set_edad(self,edad):
        self.edad= edad
        
    def set_peso(self,peso):
        self.peso= peso

    
#definir una instancia de tipo Animal para un objeto llamado caballo
caballo = Animal("Zeus","Pura sangre",5,450.0)

#definir una instancia de tipo Animal para un objeto llamado leon
leon = Animal("Boulder","Atlas",10,130.0)

print(caballo.get_peso())
# print(leon.get_raza())
