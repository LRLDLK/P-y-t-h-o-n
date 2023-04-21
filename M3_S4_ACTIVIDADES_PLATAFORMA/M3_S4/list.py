#listas en py
#--------------
#estructura para almacenar datos con un orden especifico de insercion

lista = [1,2,3,4,0]
lista_diferentes_valores = [1,"2","4",1.5,True,False,lista]


print(lista_diferentes_valores[6])

#el indice -1 de la lista es el 4
print(lista[2])

#algunos metodos de las listas
#agregar, anexar valor
#nombre.append()
lista.append(5)
print(lista)

#remove por elemento existente en la lista .remove(elemento)
lista.remove(5)
print(lista)

#pop elimina por indice
a = lista.pop(1)
print(a)
print(lista)

#insercion por indice insert(indice,valor)
lista.insert(1,2)
print(lista)

#indice por elemento index(elemento)
indice = lista.index(2)
print(indice)

#ordenar por elementos dentro la lista
lista.sort()