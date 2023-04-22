'''
EJERCICIO
Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, 
e imprimir en pantalla las consonantes restantes 
y su posición dentro de dicha palabra.
'''

#palabra en variable
palabra = "paralelepípedo"

#lista de vocales de condicion
vocales = 'aeoí'

#las consonantes solas en variable vacia
consonantes = ''



for i in range(len(palabra)):
    if(palabra[i] not in vocales):
        consonantes += palabra[i]
        print(f"La letra {palabra[i]} se encuentra en la posición {i}")
        
print(consonantes)


