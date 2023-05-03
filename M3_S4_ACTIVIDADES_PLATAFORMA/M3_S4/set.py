#SET 
#----
# coleccion de elementos y son unicos 
# se define utilizando al funcion set()
# se puede defini con {} pero se inicializa como un diccionario"

# convertir lista a set
lista = [1,2,3] #lista
lista = set(lista) #declarando un set(elemento) set({1,2,3})
print(lista)

#una manera de crear un set
nombre_set = set({1,2,3,4,5,6,7,8,9,10,11})

# no acepta valores repetidos
set = {1,1,2,3}#imprime {1, 2, 3}
print(set)

#metodos de set
# --------------

#añadir .add(elemento)
set.add(4)
print(set)

#remover .remover(elemento)
set.remove(1)
print(set)

#interseccion de elementos
elementos_comunes = nombre_set.intersection(lista)
print(elementos_comunes)

#diferencia simetrica entre set
element_unicos = nombre_set.symmetric_difference(lista)
print(element_unicos)

#selementos diferentes
elementos_diferentes = nombre_set.difference(lista)
print(elementos_diferentes)

print("-----------------PARTE 2-----------------")
set_datoss = set({10,20,14,3})

#se puede inicializar como un dccionario
my_set = {}

#verificar o ver el tipo de dato de un set
print("El tipo de dato de set_datoss es: ", type(set_datoss))#class set
print("El tipo de dato de set_datoss es: ", type(my_set))#class dict

#busqueda elementos en un set, retorna true o false
print("busqueda del numero 1' en ser_datoss: ", 10 in set_datoss)

#remover todos o borrar el set,
#my_set.clear()
#print("my_set: ", my_set )

my_set ={50, 100, 200}
new_set = set_datoss.union(my_set)
print("new_set: ", new_set)
print("imprimiendo retorno del nuevo set: ", set_datoss.union(my_set))

#inteseccion() => entrega datos existente s dento dos set
interseccion_set  = new_set.intersection(my_set)
print("interseccion_set: ", interseccion_set)

#diferencias (set a comprarar)m retoran unnuevo set con dats diferentes entre lso set
diferencias_set = new_set.difference(my_set)
print("difference: ", diferencias_set)

#conversion
my_set = list(my_set)
set_datoss = tuple(set_datoss)
print("my_set convertido a lista: ", my_set)
print("set_datos convertido a tupla: ", set_datoss)