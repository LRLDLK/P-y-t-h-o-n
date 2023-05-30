"""
EJERCICIOS:
Partiendo del ejercicio anterior (Rebound Exercises), 
construya una función que reemplace el contenido de “Información” por “Procesamiento”, 
e imprima cuántos reemplazos realizó en el archivo.

Teniendo como salida lo siguiente:

$ $ python ejercicio.py
Se realizaron: 5 remplazos

El contenido del archivo informacion.dat es:

Datos de Procesamiento en la línea 1
Datos de Procesamiento en la línea 2
Datos de Procesamiento en la línea 3
Datos de Procesamiento en la línea 4
Datos de Procesamiento en la línea 5
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada
"""

def reemplazando_informacion(texto_antiguo, texto_nuevo):
    cantidadReemplazos = 0
    try:
        archivo = open('informacion.dat','r', encoding='utf-8') ##aperturar archivo
        lineas = archivo.readlines() ##leer lineas
        archivo.close()        ##cerrar archivo
        reemplazos = '' ##acumular las lineas reemplazadas
        for l in lineas: ##se recorre las lista de lineas
            if texto_antiguo in l: ##se verifica si el texto viejo eiste ne la linea que se recorre
                l = l.replace(texto_antiguo, texto_nuevo) ##se reemplaza el texto antiguo con el texto nuevo
                reemplazos += l ##se cuenta el reemplazo
                cantidadReemplazos += 1 ##se acumula la linea
            else:
                reemplazos += l           ##para no eliminar las lineas (del final) que no se reemplazan y queden incluidas despues de los reemplazos
        if cantidadReemplazos > 0: ##se verifica el contado si se reemplazaron lineas
            archivo_reemplazo = open('informacion.dat','w', encoding='utf-8') ##se apertura
            archivo_reemplazo.write(reemplazos) ## se escribe en el archivo
            archivo_reemplazo.close() ##se cierra el archivo
    except FileNotFoundError:
        print('No se encontró el archivo')
    except Exception as e:
        print('ERROR: se ha generado un error no previsto', type(e).__name__)
    finally:
        print(f'se realizaron {cantidadReemplazos} reemplazos')
        
reemplazando_informacion('Información', 'Procesamiento')            
                
                 