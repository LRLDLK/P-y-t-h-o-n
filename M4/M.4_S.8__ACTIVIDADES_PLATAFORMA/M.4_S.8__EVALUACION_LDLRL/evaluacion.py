"""
EJERCICIOS:
Partiendo de la actividad realizada en el Rebound Exercises, 
construya una función que lea el
contenido del archivo informacion.dat.

Teniendo como salida lo siguiente:

$ python ejercicio.py
El archivo informacion.dat ya existe, ha sido creado previamente
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
        #file.readline()   #no se puede leer si se está escribiendo el archivo
        file.close()    
    except FileExistsError:
        print('ERROR: El archivo *informacion.dat* ya existe, ha sido creado previamente')
    except Exception as e: #otros errores
        print(f'ERROR:{e}')
        


def leer_archivo():
    try:
        with open('informacion.dat','r') as file:
            datos = file.readlines()
            for linea in datos:
                #print(linea,end="")
                print(linea.strip()) #cortar espacios delante y final
    except FileNotFoundError:
        print('ERROR: archivo no encontrado')
        
#escribir datos dentro el archivo
def escribir_archivo(lista):
    try:
        with open('informacion.dat','w',encoding='utf-8') as file:
            for dato in lista:
                file.write(dato+'\n')
    except FileNotFoundError:
        print('ERROR: No se encuentra el archivo a escribir')

lista = ['Datos de Procesamiento en la línea 1',
'Datos de Procesamiento en la línea 2',
'Datos de Procesamiento en la línea 3',
'Datos de Procesamiento en la línea 4',
'Datos de Procesamiento en la línea 5',
'Datos de Procesamiento en la línea 6']

crear_archivo()
escribir_archivo(lista)    
leer_archivo()
            