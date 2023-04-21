'''
EJERCICIO
Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra
“ejercicio”. Luego, crear un set que contendrá cada una de las variables que creamos, y será
asignado a una variable.
A continuación, crearemos una lista que contendrá el set creado anteriormente, y una variable con
el valor lógico False. Esta lista la asignaremos a una variable que luego imprimiremos en pantalla 
'''

#asignar variables
num1 = 8
num2 = 10.5
palabra = "ejercicio"

#crear set
crea_set = {num1, num2, palabra}

#crear lista
variable = False
crea_lista = [crea_set,variable] 

#imprimir lista
print (crea_lista)

