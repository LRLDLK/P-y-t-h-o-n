'''
EJERCICIO
Escribir un programa que analice un número, e indique si es positivo o negativo, 
y si es par o impar.
En caso de ser cero, también indicarlo. 
Se debe usar la expresión if-elif-else, y no usar subcondiciones; 
en su lugar, usar condiciones anidadas.
'''

# recibiendo el numero en variable

numero = (input("Ingresa un numero entero: "))
# verificar si es cero
# verificar que sea postivo (mayor a cero)
# verificar si es positivo par, si es positivo impar
# verificar si es negativo par, si es negativo impar
# imprimir
try:
    numero = int(numero)
    if numero == 0:
        print(f"El número {numero} es igual a cero")
    else:
        if numero > 0:
            if (numero % 2) == 0:
                print(f"El número {numero}, es positivo y par")
            else:
                print(f"El número {numero}, es positivo e impar")
        else:           
            if (numero % 2) == 0:
                print(f"El número {numero}, es negativo y par")
            else:
                print(f"El número {numero}, es negativo e impar")
except ValueError:
    print("Lo ingresado NO es un número entero")


# otra resolucion
  
        
    