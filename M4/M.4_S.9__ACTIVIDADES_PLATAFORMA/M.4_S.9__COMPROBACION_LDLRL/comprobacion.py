"""
EJERCICIO:
Diseñe un programa en Python que agregue el siguiente contenido al archivo: informacion.dat.

Hola Mundo
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada

El nuevo archivo contiene la siguiente información:

Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada
"""

def agregando_informacion(texto):
    try:
        with open("informacion.dat","a", encoding="utf-8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("ERROR: No se encontro el archivo")
    except Exception as e:
        print("ERROR: ", e)
    

agregando_informacion('Hola Mundo')
agregando_informacion('Este en una nueva línea en el archivo')
agregando_informacion('agregando la segunda línea del archivo')
agregando_informacion('finalizando la línea agregada')
            

