'''
EJERCICIO
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
'''

#recibiendo el numero en variable
numero = int(input("Ingresa un numero: "))

#verificar que sea postivo (mayor a cero)
#determinar que esté en un rango entre 1 el numero 
#multiplicar en cada iteracion la variable factorial que empieza en uno por el valor incrementado 
#imprimir 
if numero >= 0:
    factorial = 1

    for i in range(1,numero+1):
          factorial = factorial * i

    print(f"El factorial de {numero} es: {factorial}")

else:
    print(f"No se pude calcular el factorial de {numero}, porque es un número negativo")
        
        
#otra resolucion
num = 0

while True:
    num = int(input("Ingresa un numero entero mayor a cero: "))
    if(num > 0):
        break
    
factorial2 = 1
i=1

while True:
    #acummulando el factorial por cada valor del iterador
    factorial2*=i
    #cambiando el valor del iterador
    i += 1
    if i>num:
        break

print(f"El factorial de {num} es: {factorial2}")

# otra resolucion con libreria math
import math

nume = 4
factorial3= math.factorial3(nume)
print(f"El factorial de {nume} es: {factorial3}")