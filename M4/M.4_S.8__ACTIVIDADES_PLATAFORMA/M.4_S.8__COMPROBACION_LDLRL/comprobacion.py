"""
EJERCICIO:
Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el
archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente
creado.

El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:

Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
"""


#crear arhivo
def crear_archivo():
    try:
        file = open('informacion.dat','x') #crear el archivo y se apertura 
        file.readline()   #no se puede leer si se está escribiendo el archivo
        file.close()    
    except FileExistsError:
        print('ERROR: El archivo ya existe')
    except Exception as e: #otros errores
        print(f'ERROR:{e}')
        
crear_archivo()