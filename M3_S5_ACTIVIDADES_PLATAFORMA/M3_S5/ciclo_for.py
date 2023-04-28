#--------
# ciclo
# -------

#ejecutan instrucciones repetitivas hasta que se cumpla una condicion, 
# se finalice el ciclo loop


#ciclo for
#----------
#for i in data:
#   instrucciones a realizar

frutas =["pera","kiwi","piña"]

for i in frutas:
    print(i)
    
#for i in range:
#   instrucciones a realizar
for i in range(1,6):
    print(i)
    
#conocemos los elementos
for i in range(len(frutas)):
    print(i)

#conocemos los elementos y la posicion
palabra = "python"
for i in range(len(palabra)):
    print(palabra[i])
    
    
#------------
#ciclo FOR
#------------
#se utiliza para el recorrido de datos, en listas, tuplas, diccionarios, set, string
#se utiliza el metodo range() para obtener el rango hasta donde se debe recorrer
#se utiliza el metodo len() para obtener el tamño de la estructura que se recorre

#indice [0,1,2,3,4,5]
lista=[1,2,3,4,5,6]

#recorriendo o conociendo los elementos de la lista
for item in lista:
    print("Recorriendo el elemento de la lista ", item)
    
#recorriendo o conociendo el indice de la lista
for item in range(len(lista)):
    print("Recorriendo el indice de la lista ", item)
    
#recorriendo o conociendo el indice de la lista
for item in lista:
    print("Recorriendo el elemento de la lista ", lista.index(item))
    
print("---------------------EJERCICIO 1-----------------------------------")
contador=0    
for item in lista:
    print("Recorriendo el elemento de la lista ", item) 
    if(item == 1):
        contador +=1
        print("existe el nro")
print(contador)

print("---------------------------DICCIONARIOS-----------------------------")
#DICCIONARIO
#-----------

diccionario = {"a":2, "b":2,"c":3,"d":4}

#obteniendo el valor de una key
for item in diccionario:
    print("valos de la clave", item)
    
#oteniendo valor de una clave
for item in diccionario:
    print("valor", diccionario[item])
    
#obteniendo solo valores
for item in diccionario.values():
    print("obteniendo el valor", item)

#obteniendo solo 
for item in diccionario.items():
    print("obteniendo todo el elemento", item)