#SET 
#----
# coleccion de elementos y son unicos 

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

