'''
EJERCICIO
Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente,
imprimiremos en pantalla la lista.
'''
#registro en diccionarios
persona_uno = {
    "nombre" : "Alfa",
    "apellido": "Beta",
    "telefono": 2345678  
}

persona_dos = {
    "nombre" : "Gamma",
    "apellido": "Delta",
    "telefono": 1234567  
}

persona_tres = {
    "nombre" : "Lambda",
    "apellido": "Omega",
    "telefono": 3456789  
}

#agregar diccionarios a lista
registros = [persona_uno,persona_dos,persona_tres]

# imprimir lista
print (f"Registro de datos : {registros}")
