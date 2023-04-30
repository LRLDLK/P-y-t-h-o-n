# EJERCICIO
# PASO A: Crear una función que acepte 3 números como parámetros, sume todos los valores,
# y adicionalmente reste el segundo y tercer parámetro al primero.
# PASO C: Al invocar la función, debemos pasarle los parámetros en forma de lista. 
# PASO B: Esta devolverá ambos resultados en una tupla. 
# Los resultados se deben imprimir en pantalla

numeros = []
contador = 1

#PASO A:
while len(numeros) != 3:
        numero = input("Ingrese 3 números separados por un guion, sin espacios: ") 
        if(len(numero)) == 5:
                for num in [float(n) for n in numero.split("-")]:
                        numeros.append(num)      
        else:
                print("El dato ingresado es inválido, ingrese nuevamente")     
        
#  PASO B: operaciones        
def operaciones(numeros):
        suma = 0 
        for n in numeros:
                suma  += n
                resta = numeros[0] - (numeros[1]+numeros[2])
        tupla_resultado = (suma, resta)
        tupla_resultado = tuple(tupla_resultado)
        print("____________________________________________________________")
        print(f"Comprobando el tipo ** {type(tupla_resultado)} **\n")
        print(f"Los resultados en una tupla, de las operaciones de los números ingresados, son:\n(suma, resta):")        
        return tupla_resultado
        
#PASO C:
print(operaciones(numeros))
print("____________________________________________________________")