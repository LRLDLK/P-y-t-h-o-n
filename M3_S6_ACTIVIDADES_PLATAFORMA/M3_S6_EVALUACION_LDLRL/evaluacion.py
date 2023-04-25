'''
EJERCICIO
Se requiere contar con un programa que, dados 3 números diferentes,
los evalúe y entregue el orden de mayor a menor.
'''
numeros = []
contador = 1
# Mientras no se hayan leído 3 números...
while len(numeros) < 3:
    # Hacemos un ciclo infinito que se romperá solo cuando estén los tres números ingresados correctamente:
    numero = input("Ingrese el número entero " + str(contador) + ": ")

    try:
            numero = int(numero)       
            # Si todo es correcto, agregamos el número al arreglo
            numeros.append(numero)
            # Y aumenta el contador
            contador = contador + 1
    except ValueError:
        print("Lo ingresado NO es un número entero")

# ordenar los  3 números

for i in numeros:
    for j in range(len(numeros) - 1):
        if numeros[j] < numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
# ordenados se imprimen
for numero in numeros:
    print(numero)
