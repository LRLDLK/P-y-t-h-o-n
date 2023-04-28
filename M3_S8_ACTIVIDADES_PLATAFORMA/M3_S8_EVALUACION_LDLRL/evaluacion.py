# EJERCICIO
# Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
# 1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
# • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
# • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
# • Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
# segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
# • Finalmente, imprimiremos en pantalla el diccionario resultante.
# Ejemplo de impresión en pantalla:
# A:[1, 2, 3]

lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

print(f"Imprimiendo cada dato resultante: ")
for l in lista:
    if l[0] == 0:
        continue    
    for n in l:        
        if n  == 0:
            continue       
        print(n)
        

print("-----------------DICCIONARIO---------------------")
diccionario = dict()
nombre=['A','B','C','D']
indice = 0

for d in lista:
    for n in nombre:    
        diccionario[nombre[indice]] = lista[indice]
    indice+=1
#print(diccionario) 
#=>{'A': [1, 2, 3], 'B': [0, 4, 5], 'C': [4, 0, 1], 'D': [6, 5, 4]}
print("Imprimiendo las sublistas dentro del diccionario: ")
for x,y in diccionario.items():
    print(f"{x}: {y}")  