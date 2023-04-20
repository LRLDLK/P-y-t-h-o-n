#los modulos son importados dentro del proyecto, como librerias que realizan alguna accion
#ejemplo modulo math
#se importan en la parte superior del proyecto segun a continuacion:
#math es una librerira ya existente en py, que es para operaciones matematicas y aritmeticas
#provee algunas funciones o metodos
from math import pi as PI_VALUE #IMPORTANDO UNA LIBRERIA ESPECIFICA DE math as (para asignar un alias)
from math import * #IMPORTANDO TODO LO QUE CONTIENE LA LIBRERIA math, * (asterisco para todos los elementos)
import math #IMPORTANDO LA LIBRERIA math POR COMPLETO
#ejemplo de operacion
math.sqrt(2)#calcula la raiz cuadrada de 2
print (math.exp(2)) # calcula el exponente de 2, con print para ejecutar o imprimir la operacion 
math.pow(2,3) #calcula la protencia de 2 a la 3

