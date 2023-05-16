"""
EJERCICIOS:
Realice los pasos que se detallan a continuación:
1. La clase Libro está definida. Cree dos instancias de la clase Libro denominadas libro_1 y
libro_2. Luego, asigne atributos de instancia a estos objetos (usando la notación de
puntos) de la siguiente manera:
● libro_1:
○ autor = 'Dan Brown'
○ titulo = 'Infierno'
● libro_2:
○ autor = 'Dan Brown'
○ titulo = 'El Código Da Vinci'
○ ann_de_publicacion = 2003
2. En respuesta, imprima el valor del atributo __dict__ de libro_1 y libro_2.
3. Resultado al ejecutar:
1
2
print(libro_1.__dict__)
print(libro_2.__dict__):
Salida:
1
2
3
{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title
"""

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
