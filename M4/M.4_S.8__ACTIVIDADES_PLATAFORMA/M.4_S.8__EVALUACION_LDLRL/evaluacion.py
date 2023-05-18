"""
EJERCICIOS:
1. Defina una clase que contiene el objeto Persona con un solo atributo nombre. Luego, se
crean dos subclases: Maratonista y Ciclista, que pertenecen a la clase Persona.
2. Cada Clase contiene un método que se llama movimiento. Para el caso de la Persona, el
estado de movimiento es “caminando”, para el caso del Maratonista es “trotando”, y para
el caso del Ciclista es “rodando”.
3. Diseñe la clase en Python que refleje la herencia antes descrita.
"""

class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura    
        self.peso = peso


#getter and setters son funciones para obtener o dar valor a los atributos:

#getters
    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos
    
    def get_sexo(self):
        return self.sexo
    
    def get_edad(self):
        return self.edad    
    
    def get_estatura(self):
        return self.estatura
    
    def get_peso(self):
        return self.peso

#setters
    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_apellidos(self,apellidos):
        self.apellidos = apellidos

    def set_sexo(self,sexo):
        self.sexo = sexo
        
    def set_edad(self,edad):
        self.edad = edad    
    
    def set_estatura(self,estatura):
        self.estatura = estatura

    def set_peso(self,peso):
        self.peso = peso
        

#instanciar persona
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)


# Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se
# muestre por pantalla las actualizaciones respectivas. 

#get (obtener) el valor del atributo antes de modificar
print("-------- Datos originales -----------")
print(f"La edad de persona_1 con nombre {persona_1.nombre} se define con {persona_1.get_edad()} años \n")
print(f"El apellido de persona_2 con nombre {persona_2.nombre} se define como {persona_2.get_apellidos()}")

#setear (cambiar) valor atributo
persona_1.set_edad(21)
persona_2.set_apellidos("Santiago")

#get (obtener) el valor del atributo después de modificar
print("-------- Datos modificados -----------")
print(f"La edad de persona_1 con nombre {persona_1.nombre} se ha modificado a {persona_1.get_edad()} años \n")
print(f"El apellido de persona_2 con nombre {persona_2.nombre} se se ha modificado a {persona_2.get_apellidos()}")


