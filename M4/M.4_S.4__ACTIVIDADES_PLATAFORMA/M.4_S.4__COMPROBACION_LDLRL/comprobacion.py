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
1 print(libro_1.__dict__)
2 print(libro_2.__dict__):


Salida:
1{'author': 'Dan Brown', 'title': 'Inferno'}
2{'author': 'Dan Brown', 'title': 'The Da Vinci Code',
3'year_of_publishment': 2003}
"""

from multipledispatch import dispatch
class Libro:

    def __init__(self, autor=None, titulo=None, ann_de_publicacion=None):
        self._autor = autor
        self._titulo = titulo
        self._ann_de_publicacion = ann_de_publicacion
 
        
#getter and setters son funciones para obtener o dar valor a los atributos:
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    
    @property
    def ann_de_publicacion(self):
        return self._ann_de_publicacion
    
    @ann_de_publicacion.setter
    def ann_de_publicacion(self, ann_de_publicacion):
        self._ann_de_publicacion = ann_de_publicacion
        
    def __str__(self) -> str:
        return f"Autor: {self._autor}, Titulo: {self._titulo}, Año de publicación: {self._ann_de_publicacion}"
    
libro_1 = Libro('Dan Brown','Infierno')
libro_2 = Libro('Dan Brown','El Código Da Vinci', 2003)

#__dict__ imprimir como diccionario
print(libro_1.__dict__)
print(libro_2.__dict__)

print("----------------")
print(libro_1)
print(libro_2)

