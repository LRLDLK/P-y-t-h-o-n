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
                # Si todo es correcto, agrega número al arreglo
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
    
#otra solucion


