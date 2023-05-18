from trabajador import Trabajador
from departamento import Departamento
from persona import Persona


trabajador = Trabajador('Juan','Pérez','2005','Ingeniería de software','IS','20000')


print(trabajador.__dict__)

print('Es trabajador instancia de Persona: ',isinstance(trabajador, Persona))
print('Es trabajador instancia de Departamento: ',isinstance(trabajador, Departamento))
print('Es trabajador instancia de Trabajador: ',isinstance(trabajador, Trabajador))