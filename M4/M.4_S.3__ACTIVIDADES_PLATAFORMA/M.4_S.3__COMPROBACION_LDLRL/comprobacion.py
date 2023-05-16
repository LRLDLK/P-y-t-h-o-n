# EJERCICIO:
# Realice un diagrama de clases que simule a una persona y a un estudiante. La persona contiene las
# siguientes características: número de identificación, el nombre, el apellido. Mientras que el
# estudiante contiene el número de identificación, el nombre, el apellido, código del alumno y matrícula.
# Ambos poseen un método para obtener los datos. 

from multipledispatch import dispatch
class Animal:
    

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
