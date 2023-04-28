# EJERCICIO
# Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
# 1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# PASO C:#   Se debe ----imprimir cada dato---- de las listas en pantalla con las siguientes excepciones:
# PASO A:# • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
# PASO B:# • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.

lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
#PASO A:
lista_dos = []
for i in lista:
    if(i[0] != 0):
        lista_dos.append(i)
#print(lista_dos) 
# => [[1, 2, 3], [4, 0, 1], [6, 5, 4]]        
#PASO B:  
lista_final = []
for lista in lista_dos:
    for j in lista:
        if j !=0:
            lista_final.append(j)
#print(lista_final) 
# => [1, 2, 3, 4, 1, 6, 5, 4]
#PASO C:
print(f"Imprimiendo cada dato resultante: ")
for k in (lista_final):
    print(k)
    
#otra solucion
# listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# for l in listas:
#     if l[0] == 0:
#         continue
#     for n in l:
#         if n  == 0:
#             continue
#         print(n)
        
#----------------------
# mi_lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]] 
# resultados = [] 


# for numeros in mi_lista:     
#     sublista = [] 
#     j = 0 
#     for valor in numeros: 
#         if valor == 0 and j == 0: 
#             break 
#         elif valor == 0 and j != 0: 
#             continue 
#         else: sublista.append(valor) 
#         j += 1 
#     if sublista: 
#         resultados.append(sublista) 

# print(resultados)    

