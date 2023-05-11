# EJERCICIO
# PASO A: Crear una función que acepte 3 números como parámetros, 
# PASO B: sume todos los valores, y adicionalmente reste el segundo y tercer parámetro al primero.
# PASO C: Al invocar la función, debemos pasarle los parámetros en forma de lista. 
# PASO B-C: Esta devolverá ambos resultados en una tupla. 
# Los resultados se deben imprimir en pantalla



#PASO A:
# Mientras no se hayan ingresado 3 números a la lista...
def datos():
        numeros = []
        contador = 1
        while len(numeros) < 3:
        #  ciclo infinito que se romperá solo cuando estén los tres números ingresados correctamente:
                numeroFloat = input("Ingrese el número N°" + str(contador) + ": ")  
                try:    
                        numero = float(numeroFloat)   
                        numeros.append(numero)
                        # Y aumenta el contador
                        contador += 1
                except ValueError:
                        print("Lo ingresado NO es válido")               
        return numeros

#PASO B: operaciones
def operaciones(lista):
        suma = 0 
        for n in lista:
                suma  += n
                resta = lista[0] - (lista[1]+lista[2])
        tupla_resultado = (round(suma,2), round(resta,2))
        tupla_resultado = tuple(tupla_resultado)                
        return(tupla_resultado)

#PASO C: 
num = datos()
resultados = operaciones(num)

print("___________________________________________________________________________") 
print(f"Los resultados en una tupla, de las operaciones de los números ingresados:\n(SUMA de los 3, RESTA {num[0]} - ({num[1]} + {num[2]}) \n=> {resultados}")
print(f"=> Comprobando el tipo tupla: ** {type(resultados)} **") 
print("___________________________________________________________________________")

