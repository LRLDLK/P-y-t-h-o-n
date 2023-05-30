"""
EJERCICIOS:
Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de
una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se
lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000.

Ejemplo de la salida del programa:

Ingrese el salario: 5000
Traceback (most recent call last):
 File "drilling-CUE07.py", line 20, in <module>
 raise RangoSalarioError(salario)
__main__.RangoSalarioError: 5000 -> Salario no está definido en el
rango (1000 a 2000)
"""
# Define clase a partir de Exception
class RangoSalarioError(Exception):
    '''Excepción definida'''    
    def __init__(self, msj):  # define método constructor ...   
        Exception.__init__(self)  # … de excepción ... 
        self.msj = msj # … y con atributo msj

class RangoSalarioCorrecto(Exception):
    def __init__(self, msj):  # define método constructor ...   
        Exception.__init__(self)  # … de excepción ... 
        self.msj = msj # … y con atributo msj        
         
def salario():
    rango = "(1000 a 2000)"
    while True:
        try:  # bloque de código a controlar
            salario = int(input('Ingrese el salario: '))  # introducir una cadena
            if salario not in range(1000,2001):  # si longitud de cadena no esta en el rango
                raise RangoSalarioError('ERROR: '+str(salario)+' --> Salario NO está definido en el rango: '+ rango)  # llama a excepción de usuario 
            else:
                raise RangoSalarioCorrecto('CORRECTO: '+str(salario)+' --> Salario SI está definido en el rango '+rango)
        except RangoSalarioError as e:  # excepción de usuario   
            print(e.msj)        
        except RangoSalarioCorrecto as e:  # excepción de usuario   
            print(e.msj)
            break
        except ValueError:
            print('ERROR: Ingreso inválido. Ingrese el salario nuevamente')

      

if __name__ == "__main__":
    salario()
    