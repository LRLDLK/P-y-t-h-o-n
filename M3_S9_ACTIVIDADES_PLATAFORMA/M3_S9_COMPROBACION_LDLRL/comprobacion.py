# EJERCICIO
# PASO A: Crear una función que acepte 3 números como parámetros, sume todos los valores,
# y adicionalmente reste el segundo y tercer parámetro al primero.
# Al invocar la función, debemos pasarle los parámetros en forma de lista. 
# PASO B: Esta devolverá ambos resultados en una tupla. 
# Los resultados se deben imprimir en pantalla

numeros = []
contador = 1
suma = 0
# Mientras no se hayan leído 3 números...
while len(numeros) < 3:
    #  ciclo infinito que se romperá solo cuando estén los tres números ingresados correctamente:
    numero_ingresado = input("De 3 números, ingrese el número N°" + str(contador) + ": ")
 
    try:
            numero = float(numero_ingresado)
            # comprobación si el número existe
            numeros.append(numero)
            contador += 1
    except ValueError:
        print("Lo ingresado NO es un número válido")

#  PASO B: operaciones

for n in numeros:
        suma  += n
        resta = numeros[0] - (numeros[1]+numeros[2])
tupla_resultado = (suma, resta)
print("El resultado de las operaciones en una tupla es: ")
print(tupla_resultado)
print(f"Comprobando el tipo ** {type(tupla_resultado)} **")

