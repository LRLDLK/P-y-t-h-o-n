from persona import Persona
from departamento import Departamento

class Trabajador(Persona, Departamento):   
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario) -> None:
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self._salario = salario

    @property
    def _salario(self):
        return self.salario
    
    @_salario.setter
    def _salario(self, salario):
        self.salario = salario        
   
    def __str__(self) -> str:
        return f"Nombre: {self._nombre}, Apellido: {self._apellido}, Año: {self._anno}, Nombre Depto.: {self._nombre_dpto}, Nombre corto Depto.: {self._nombre_corto_dpto}, Salario: {self._salario}"
    
    