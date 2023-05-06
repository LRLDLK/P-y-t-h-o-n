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
# PASO A: Debemos separar los nombres en tres grupos: magos, científicos y otros; 
# PASO B: y escribir una función llamada hacer_grandioso(), 
# que modifique la lista de magos añadiendo la frase ‘El gran‘ 
# antes del nombre de cada mago.
# PASO C: Crear una función llamada imprimir_nombres(), 
# que imprime el nombre de cada persona de la lista.
# PASO D: Finalmente, imprimir en pantalla la lista completa de nombres  antes de ser modificados; 
# PASO E: luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# PASO A:
def listas(lista):
    magos = []
    cientificos = []
    otros = []
    for l in lista:
        if l in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(l)
        elif l in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(l)
        elif l in ['Messi','Pele','Juanes']:
            otros.append(l)
    return magos, cientificos, otros

#PASO B:
def hacer_grandioso(magos):
    nombre ='El gran '
    indice= 0
    magos_grandiosos =[]
    for indice, item in enumerate(magos):
        if item:
            magos[indice] = nombre+magos[indice]                              
        indice+=1
    magos_grandiosos.append(magos)         
    return  magos_grandiosos

#PASO C:
def imprimir_nombres(nombres):
    for n in nombres:
       print('•',n)   
   
#PASO D:
print('------------------------------------------------')
print('-----------------LISTA ORIGINAL-----------------')
print('------------------------------------------------')
print('La lista original de los nombres es: \n')
imprimir_nombres(lista)

#PASO E:
print('---------------------------------------------')
print('-----------------LISTA FINAL-----------------')
print('---------------------------------------------')
print('La lista final de los nombres es: \n')
print('La lista de *magos grandiosos* es : ')
magos, cientificos, otros = listas(lista)
magos_grandiosos = hacer_grandioso(magos)
for m in (magos_grandiosos):
    imprimir_nombres(m)
print('La lista de *científicos* es : ')
imprimir_nombres(cientificos)
print('La lista de *los restantes* es : ')
imprimir_nombres(otros)
print('---------------------------------------------')
print('---------------------------------------------')
print('---------------------------------------------')
