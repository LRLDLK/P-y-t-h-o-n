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
cientificos = [ 'Newton', 'Hawking', 'Einstein']
otros = ['Messi','Pele','Juanes']

magos_grandiosos = []

nombre ="El gran "
indice= 0

def hacer_grandioso():
    for indice, item in enumerate(magos):
        if item:
            magos_grandiosos.append(nombre+magos[indice])                    
        indice+=1         
    return  magos_grandiosos

hacer_grandioso()


def imprimir_nombres():
    for m in magos:
        print(m)
    for c in cientificos:
        print(c)
    for o in otros:
        print(o)


print("-----------------LISTA ORIGINAL-----------------")
print("La lista original de los nombres es: ")
imprimir_nombres()

print("-----------------LISTA FINAL-----------------")
print("La lista final de los nombres es: ")
for m in magos_grandiosos:
        print(m)
for c in cientificos:
    print(c)
for o in otros:
    print(o)
    
