"""
EJERCICIO:
Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresar
un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que
ingrese su edad nuevamente.
Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso
contrario, no es un adulto.
"""

while True:
    try:
        edad = int(input('Ingrese su edad: '))
        break
    except ValueError:
        print('ERROR: debe ser número entero, ingrese su edad nuevamente')
    except Exception as e:
        print('ERROR: ', e)        
if edad >= 18:
    print('Usted es adulto')
else:
    print('Usted no es adulto')
            