'''
EJERCICIO
Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente,
imprimiremos en pantalla la lista.
'''
#registro en diccionarios
persona1 = {
    "nombre" : "Alfa",
    "apellido": "Beta",
    "telefono": 2345678,  
}

persona2 = {
    "nombre" : "Gamma",
    "apellido": "Delta",
    "telefono": 1234567,  
}

persona3 = {
    "nombre" : "Lambda",
    "apellido": "Omega",
    "telefono": 3456789,  
}

#agregar diccionarios a lista
registros = [persona1,persona2,persona3]

# imprimir lista
print (f"Registro de datos : {registros}")
