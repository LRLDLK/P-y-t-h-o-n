# FILTRANDO DATOS
# INSTRUCCIONES
# Lee con atención cada uno de los requerimientos que se presentan a continuación,
# y desarrolla la prueba de acuerdo con lo solicitado.
# DESCRIPCIÓN
# Dada la siguiente lista de nombres:
# • Harry Houdini
# • Newton
# • David Blaine
# • Hawking
# • Messi
# • Teller
# • Einstein
# • Pele
# • Juanes
# Y sabiendo que Harry Houdini, David Blaine y Teller son magos. 
# Y también que Newton, Hawking y Einstein son científicos. 
# Debemos separar los nombres en tres grupos: magos, científicos y otros; 
# PASO A: y escribir una función llamada hacer_grandioso(), 
# que modifique la lista de magos añadiendo la frase ‘El gran‘ 
# antes del nombre de cada mago.
# PASO B: Crear una función llamada imprimir_nombres(), 
# que imprime el nombre de cada persona de la lista.
# PASO C: Finalmente, imprimir en pantalla la lista completa de nombres  antes de ser modificados; 
# PASO D: luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

magos = ['Harry Houdini', 'David Blaine','Teller']
magos_grandiosos = ['Harry Houdini', 'David Blaine','Teller']
cientificos = [ 'Newton', 'Hawking', 'Einstein']
otros = ['Messi','Pele','Juanes']

nombre ="El gran "
indice= 0

#PASO A:
def hacer_grandioso():
    for indice, item in enumerate(magos_grandiosos):
        if item:
            magos_grandiosos[indice] = nombre+magos_grandiosos[indice]                              
        indice+=1         
    return  magos_grandiosos

hacer_grandioso()

#PASO B:
def imprimir_nombres():
    print('La lista de *magos* es : ')
    for m in magos:        
        print(m)
    print('La lista de *científicos* es : ')    
    for c in cientificos:        
        print(c)
    print('La lista de *otros* es : ')    
    for o in otros:        
        print(o)

#PASO C:
print("------------------------------------------------")
print("-----------------LISTA ORIGINAL-----------------")
print("------------------------------------------------")
print("La lista original de los nombres es: \n")
imprimir_nombres()

#PASO D:
print("---------------------------------------------")
print("-----------------LISTA FINAL-----------------")
print("---------------------------------------------")
print("La lista final de los nombres es: \n")

print('La lista de *magos grandiosos* es : ')
for m in magos_grandiosos:    
    print(m)
print('La lista de *científicos* es : ')
for c in cientificos:
    print(c)
print('La lista de *los restantes* es : ')
for o in otros:
    print(o)

print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
