from trabajador import Trabajador
from departamento import Departamento
from persona import Persona

def instancia(objeto, clase):
    return 'Es Instancia' if isinstance(objeto, clase) else 'No es Instancia'

if __name__ == '__main__':
    trabajador = Trabajador('Juan','Pérez',2005,'Ingeniería de software','IS',20_000)
    print(trabajador.__dict__)
    print('\nEs trabajador instancia de Persona... ',isinstance(trabajador, Persona) )
    print('Es trabajador instancia de Departamento... ',isinstance(trabajador, Departamento))
    print('Es trabajador instancia de Trabajador... ',isinstance(trabajador, Trabajador))
    print('\nEs trabajador instancia de Persona... ',instancia(trabajador, Persona) )
    print('Es trabajador instancia de Departamento... ',instancia(trabajador, Departamento))
    print('Es trabajador instancia de Trabajador... ',instancia(trabajador, Trabajador))

