# EJERCICIO
# PASO A: Crear una función que sume dos números, otra que reste dos números, 
# otra que multiplique dos números, y otra que divida dos números. 
# PASO B: Adicionalmente, crear una función que acepte dos números como parámetros 
# y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división.
# PASO C: Los resultados se deben almacenar en un diccionario, cuyas claves serán: 
# Suma, Resta, Multiplicación y División, 
# y los valores de cada clave serán los resultados obtenidos con la función creada anteriormente.

num_1= float(input('Ingrese el primer número entero: ')) 
num_2= float(input('Ingrese el segundo número entero: '))
nombre = ['Suma', 'Resta', 'Multiplicación', 'División']   
diccionario = dict()
indice = 0
resultados =[]

#PASO A:
print("--------------OPERACIONES ARITMÉTICAS--------------")
def sumar():
    suma = num_1 + num_2
    return suma 
#sumar = lambda a, b: a + b
print(f"La suma de los números {num_1} y {num_2} es:  {sumar()}")

def restar():
    resta = num_1 - num_2
    return resta 
print(f"La resta de los números {num_1} y {num_2} es:  {restar()}")

def multiplicar():
    multiplica = num_1 * num_2
    return multiplica 
print(f"La multiplicación de los números {num_1} y {num_2} es:  {multiplicar()}")

def dividir():
    divide = num_1 / num_2
    return divide 
print(f"La división de los números {num_1} y {num_2} es:  {dividir()}")

#PASO B: 
def operaciones():
    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplica = num_1 * num_2
    divide = num_1 / num_2

    resu = (suma, resta, multiplica, divide)
    res = tuple(resu)
    #print(type(res))
     #=> <class 'tuple'>
    return res
   
  
#print(operaciones())

#PASO C:
resultados.append(operaciones())
for l in resultados:
    for k in l:
        for n in nombre:    
            diccionario[nombre[indice]] = l[indice]
        indice+=1
print("-----------------DICCIONARIO-----------------------")
print("Imprimiendo las operaciones dentro del diccionario: ")
for x,y in diccionario.items():
    print(f"{x}: {y}")  
    

   
        




    
