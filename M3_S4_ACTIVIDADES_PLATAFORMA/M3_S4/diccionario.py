#diccionarios en py
# -----------

#son una colleccion de elementos
#ordenados por clave y valor

#declaracion con llaves {} o con la funcion dict()
#usando {} como un objeto JSON

#creando o instanciando un diccionario
my_dict = dict()
other_dict = {}

#ver tipo
print("el tipo de diccionario es: ", type(my_dict))

my_dict = {
    #clave : valor
    "Nombre" : "Paquito",
    "Apellido": "Paco",
    "Edad":40,
    "Marta":50,
    "Direccion" :{
         "calle": "magnolias 123",
         "Region": "La Serena",
         "Cod.Postal": "456"
    }
}


other_dict = {
    #clave : valor
    "Nombre" : "Paquito",
    "Apellido": "Paco",
    "Edad":40,
    "Marta":50,
    "Direccion" :"magnolias 123"
}

estudiantes = {
    #clave : valor
    "Fulanito" : 20,
    "Maria":30,
    "Jose":40,
    "Marta":50,
    "ejemplo" :{
    "edad":  23, "valor":23,"otro":23
    },
}

#buscar por clave
print("Nombre: (respeta las mayusculas 'N') ", my_dict["Nombre"])

#buscar un valo dentro el diccionario
print("valor mediante clave: ", 'Paco' in my_dict['Apellido'])


print(estudiantes)

#acceder al valor de una clave
#nombre_diccionario["clave"]
print(estudiantes["Fulanito"])

#remover clave de un diccionario
del estudiantes["Fulanito"]
print(estudiantes)

#obtener todas la claves de un diccionario
claves = (estudiantes.keys())
print(claves)

#obtener todos los valores
valores=(estudiantes.values())
print(valores)

#agregar nuevo elemento
estudiantes['nuevo'] = 55
print(estudiantes)

#borrar un diccionario
#estudiantes.clear()

#diccionario dentro de otro
personas = {
  "persona_uno" : {"nombre" : "Alfa", "apellido": "Beta", "telefono": 2345678},
  "persona_dos" : {"nombre" : "Alfa", 
                   "apellido": "Beta", 
                   "telefono": 2345678, 
                   "direccion":{
                       "calle":"lalal"},
                    "region":"lelele"}
}

print(personas["persona_uno"]["nombre"])#resultado es Alfa
print(personas["persona_dos"]["direccion"]["calle"])#resultado es lalal

#actualizar valor dada una clave
my_dict["Nombre"] = "Pepito"
print("my_dict: ", my_dict)
my_dict["Direccion"]["Region"] = "El Sol"
print("my_dict: ", my_dict)

#insertar nombre[clave] = valor 
my_dict["Telefono"] = "12121212"
print("elemento insertado Telefono: en diccionario my_dict", my_dict)
#funciones de los diccionarios:
#-----------------------------

#items()
print("utilizando la funcion  items() en my_dict: ", my_dict.items())

#values()
print("utilizando la funcion values(): ", my_dict.values())

#keys()
print("utilizando la funcion keys(): ", my_dict.keys())

#crea un diccionar con las claves y valore en None
diccionario = dict.fromkeys(my_dict)
print(diccionario)

#OJO ESTA EXPLICACION NO QUEDO CLARA NO SE SABE PA QUE SIRVE
#cra un nuevo diccionario dadas las claves en tupla
otro_dict = dict.fromkeys(("Persona1", "Persona2", "Persona3"))
print(otro_dict)