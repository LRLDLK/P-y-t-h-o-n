'''
EJERCICIO:
Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad,
estatura y peso. Adicionalmente, se deben implementar los métodos get y set que modifiquen todos
los atributos antes mencionados de la clase persona, recordando que los métodos get son los
métodos que permiten acceder al estado del objeto persona, y los métodos set permiten modificar
el estado de dicho objeto.
Cree dos objetos de la instancia persona con los siguientes datos:
Persona_1: Pedro, Vivas, Masculino, 20 años, 1.78 mts, 68 Kg.
Persona_2: Juan, Camargo, Masculino. 18, 1.8 mts, 75 Kg.
Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se
muestre por pantalla las actualizaciones respectivas. 
'''


class Persona:
    def __init__(self, nombre, apellido, genero, edad, estatura, peso):
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad
        self._estatura = estatura
        self._peso = peso


# getter and setters son funciones para obtener o dar valor a los atributos:

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    def __str__(self):
        return f'Persona(nombre: {self.nombre}, apellido: {self.apellido}, genero: {self.genero}, edad: {self.edad}. estatura: {self.estatura}, peso: {self.peso})'


# instanciar persona
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)


# Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se
# muestre por pantalla las actualizaciones respectivas.

# get (obtener) el valor del atributo antes de modificar
print("-------- Datos originales -----------")
print(persona_1)
print(persona_2)
print(f"\nLa edad de persona_1 con nombre {persona_1.nombre} es {persona_1.edad} años \n")
print(f"El apellido de persona_2 con nombre {persona_2.nombre} es {persona_2.apellido}")

# setear (cambiar) valor atributo
persona_1.edad = 21
persona_2.apellido = "Santiago"

# get (obtener) el valor del atributo después de modificar
print("-------- Datos modificados -----------")
print(persona_1)
print(persona_2)
print(
    f"\nLa edad de persona_1 con nombre {persona_1.nombre} se ha modificado a {persona_1.edad} años \n")
print(
    f"El apellido de persona_2 con nombre {persona_2.nombre} se se ha modificado a {persona_2.apellido}")
