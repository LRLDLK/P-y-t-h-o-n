'''
EJERCICIO
Se requiere contar con un programa que, dados 3 números diferentes,
los evalúe y entregue el orden de mayor a menor.
'''
numeros = []
contador = 1
# Mientras no se hayan leído 3 números...
while len(numeros) < 3:
    #  ciclo infinito que se romperá solo cuando estén los tres números ingresados correctamente:
    numeroEntero = input("Ingrese el número entero N°" + str(contador) + ": ")
 
    try:
            numero = int(numeroEntero)
            # comprobación si el número existe
            if numero in numeros:
                print("El número ya existe")
            else:
                # Si todo es correcto, agrega número 
                numeros.append(numero)
                # Y aumenta el contador
                contador += 1
                
    except ValueError:
        print("Lo ingresado NO es un número entero")

#  los 3 números ordenados

for i in numeros:
    for j in range(len(numeros) - 1):
        if numeros[j] < numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
# imprimiendo
for nro in numeros:
    print(nro)

#-------------------------------------------------------------  
#otra solucion

# num_1 = int(input("Ingrese el número entero N°1: "))
# num_2 = int(input("Ingrese el número entero N°2: "))
# num_3 = int(input("Ingrese el número entero N°3: "))

# if len(set({num_1,num_2,num_3})) != 3:
#     print("Debe ingresar números distintos")
# else:
#     ordenados = sorted([num_1,num_2,num_3],reverse=True)
#     print(ordenados)

