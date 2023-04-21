#scope o alvance de una variable

#alcance global
#alcance local

#alcance global: no está dentro alguna estructura
variable_global = "se puede acceder desde todo el documento"

#metodo o funcion para ejemplificar una variable local
#def nombre_metodo(parametros_entrada):
# suma es variable local porque existe solo dentro la estrutura de la funcion
def suma(a,b):
    suma_valores = a+b
    # variable_global = suma_valores
    return suma_valores

print(suma(1,3))
print(variable_global)
# print(suma_valores) esta no accede porque es local
