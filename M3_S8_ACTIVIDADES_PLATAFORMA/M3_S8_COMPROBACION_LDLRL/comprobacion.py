# EJERCICIO
# En esta actividad trabajaremos con listas. 
# Tomando la lista que se entrega a continuación, se
# solicita realizar las siguientes acciones en el orden indicado:
# 1. Eliminar los elementos duplicados.
# 2. Ordenar la lista resultante en orden ascendente.
# La lista es:
# 1 mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
lista = sorted(list(set(mi_lista)))
print(f"La lista ordenada y sin duplicados es:\n{lista}")

#otra solucion:
# mi_nueva_lista = set(mi_lista)
#lista = sorted(list(mi_nueva_lista))

#otra solucion:
# lista= list(mi_nueva_lista)
#sort(lista)# sort arregla la actual
# print(sorted(lista))# sorted entrega nueva lista
