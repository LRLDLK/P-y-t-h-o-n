#diccionarios en py
# -----------

#son una colleccion de elementos
#ordenados por clave y valor

#declaracion con llaves {} o con la funcion dict()

estudiantes = {
    "Fulanito" : 20,
    "Maria":30,
    "Jose":40,
    "Marta":50,
    "ejemplo" :{
    "edad":  23, "valor":23,"otro":23
    },
}

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
