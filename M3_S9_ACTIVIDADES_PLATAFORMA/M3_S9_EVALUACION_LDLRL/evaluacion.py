# EJERCICIO
# PASO A: Crear una función que sume dos números, otra que reste dos números, 
# otra que multiplique dos números, y otra que divida dos números. 
# PASO B: Adicionalmente, crear una función que acepte dos números como parámetros 
# y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división.
# PASO C: Los resultados se deben almacenar en un diccionario, cuyas claves serán: 
# Suma, Resta, Multiplicación y División, 
# PASO C: y los valores de cada clave serán los resultados obtenidos con la función creada anteriormente.

num_1= 0
num_2= 0
claves = ['Suma', 'Resta', 'Multiplicación', 'División']   
contador=1

while contador < 3:
    #  ciclo infinito que se romperá solo cuando estén los 2 números ingresados correctamente:
    numeroEntero = input('Ingrese el número N°' + str(contador) + ': ') 
    try:
            numero = float(numeroEntero)
            if contador == 1:
                num_1 = numero
            elif contador == 2:
                num_2 = numero
            contador += 1              
    except ValueError:
        print('Lo ingresado NO es válido')


#PASO A:
print('--------------OPERACIONES ARITMÉTICAS---------------')
def sumar(a,b):
    suma = a + b
    return round(suma,2) 
#sumar = lambda a, b: a + b
print(f'La suma de los números {num_1} y {num_2} es:  {sumar(num_1,num_2)}')

def restar(a,b):
    resta = a - b
    return round(resta,2) 
print(f'La resta de los números {num_1} y {num_2} es:  {restar(num_1,num_2)}')

def multiplicar(a,b):
    multiplica = a * b
    return round(multiplica,2) 
print(f'La multiplicación de los números {num_1} y {num_2} es:  {multiplicar(num_1,num_2)}')

def dividir(a,b):
    if b == 0:
        return None
    else:
        divide = a / b
        return round(divide,2) 
print(f'La división de los números {num_1} y {num_2} es:  {dividir(num_1,num_2)}')

#PASO B: 
def operaciones(a,b):
    suma = sumar(a,b)
    resta = restar(a,b)
    multiplica = multiplicar(a,b)
    divide = dividir(a,b)
    resu = (suma, resta, multiplica, divide)
    res = tuple(resu)
    #print(type(res))
     #=> <class 'tuple'>
    return res
   
  
#print(operaciones())

#PASO C-1:
def resultado_final(a,b):    
    valores = (operaciones(a,b))   
    para_diccionario = zip(claves, valores)
    diccionario = dict(para_diccionario)
    for x,y in diccionario.items():
          print(f'{x}: {y}')   
   


#PASO C-2:
print('-----------------DICCIONARIO-----------------------')
print('Imprimiendo las operaciones dentro del diccionario: ')
resultado_final(num_1, num_2)
print('----------------------------------------------------')


   
        




    
