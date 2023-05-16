"""
EJERCICIOS:
1. Defina una clase que contiene el objeto Persona con un solo atributo nombre. Luego, se
crean dos subclases: Maratonista y Ciclista, que pertenecen a la clase Persona.
2. Cada Clase contiene un método que se llama movimiento. Para el caso de la Persona, el
estado de movimiento es “caminando”, para el caso del Maratonista es “trotando”, y para
el caso del Ciclista es “rodando”.
3. Diseñe la clase en Python que refleje la herencia antes descrita.
"""

from persona import Persona
from ciclista import Ciclista
from maratonista import Maratonista


persona = Persona("Alfa")
persona.movimiento("Caminando")

ciclista = Ciclista("Beta")
ciclista.movimiento("Rodando")

maratonista  = Maratonista("Delta")
maratonista.movimiento("Trotando")