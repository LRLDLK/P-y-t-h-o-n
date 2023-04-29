# calcular resistenacia de un circuito
# formula RT=1/((1/R1)+(1/R2)+(1/R3)+1(1/Rn))

# r1 = float(input("Ingrese la resistencia 1 : "))
# r2 = float(input("Ingrese la resistencia 2 : "))
# r3 = float(input("Ingrese la resistencia 3 : "))
# rT = (1/((1/r1)+(1/r2)+(1/r3)))

# print("La resistencia total es: {:.2f}".format(rT))

# otra solucion


# def validate(texto):
#     try:
#         while True:
#             r = float(input(texto))
#             if r>0:
#                 return r
#     except Exception as ex:
#         print("Ha ocurrido un error en el ingreso de la info: ", ex)
#         print("Ha ocurrido un error en el ingreso de la info, ingrese nuevamente el valor")

# r_1 =validate("Ingrese la resistencia 1 : ")
# r_2 = validate("Ingrese la resistencia 2 : ")
# r_3 = validate("Ingrese la resistencia 3 : ")

# resTot = (1/((1/r_1)+(1/r_2)+(1/r_3)))

# print("La resistencia total es: ", resTot)

# ---------------------------------------------------------

# calcular  hipotenusa req ingreso catetos a y b

# import math
# cateto_a = float(input("Ingrese valor del cateto a del tirángulo: "))
# cateto_b = float(input("Ingrese valor del cateto b del tirángulo: "))

# hipotenusa = math.sqrt(cateto_a*cateto_a + cateto_b*cateto_b)
# print(f"La hipotenusa es: {hipotenusa}")

# --------------------------------------------------------
# ingreso de 2 textos por consola y comparar si son iguales o del mismo tamaño
# ojo? .....
# texto_uno = (input("Ingresse valor del texto uno: "))
# texto_dos = (input("Ingresse valor del texto dos: "))

# if len(texto_uno) == len(texto_dos):
#     if (texto_uno == texto_dos):
#         print("Textos iguales y del mismo tamaño")
#     else:
#         print("Textos diferntes de misma longitud")
# else:
#     print("textos diferentes")

# -------------------------------------
# simulacion bonba de tiemo, ira el tiempo dek 5 al 1 . al ejecutar el programa imprimira msj boom

# import time

# i= 5

# while i >= 1:
#     print(i)
#     i-=1 # i = i - 1

# time.sleep(1)

# print("Boom!")

# --------------------------
# realizar ejecucion de un menu donde se indiquen varias opciones a seleccionar por el usuario y
# una opcion para salir del menu. usar ciclos y estructuras condicionales

# import libreria para expresiones regulares

# import re

# opcion = ""
# patron = re.compile(r"^[0-5]{1}$")
# #compilacion de patron
# while opcion != "5": #while True :
#     #impresion del menu
#     print("Hola, bienvenido, menú")
#     print("1.- Opcion 1")
#     print("2.- Opcion 2")
#     print("3.- Opcion 3")
#     print("4.- Opcion 4")
#     print("5.- Salir del menú")
#     print("Ingrese una opción")

#     opcion = input() #leyendo la opción
#     if re.match(patron,opcion):
#         if opcion == "1":
#             print("Realizando la opción 1")
#         elif opcion == "2":
#             print("Realizando la opción 2")
#         elif opcion == "3":
#             print("Realizando la opción 3")
#         elif opcion == "4":
#             print("Realizando la opción 4")
#         elif opcion == "5":
#             print("Saliendo, hasta luego")
#             #break
#         else :
#             print("Ha ingresado una opción invalida, por favor ingrese una opción")
#     else:
#         print("Ha ingresado una opcion incorrecta, valide el ingreso")

# OTRA SOLUCION

# while True:
#     opcion = int(input("Hola, bienvenido\n "
#                        "1.- Saludar\n "
#                        "2.- preguntar que hay en la tele\n "
#                        "3.- que opinas de la música que escucho?\n"
#                        "4.- que estás sintiendo ahora?\n"
#                        "5.- Salir\n\n"
#                        "Ingresa una opción => ")
#                  )

#     match opcion:
#         case 1:
#             print("Hola, que tal?")
#         case 2:
#             print("No hay nada bueno")
#         case 3:
#             print("Es buena música")
#         case 4:
#             print("Tengo hambre!")
#         case 5:
#             print("Nos vemos!")
#             break
#         case _:
#             print("Esa opcion no es válida!")
# ---------------------------------------------------
#crear una simulaciond de ingreso de una contraseña

# passw = "pass"

# intentos = 1
# while intentos <= 3:
#     clave = input(f"Ingrese la clave: ")
#     if clave == passw:
#         print("clave correcta")
#         break
#     elif intentos == 3:
#         print("Cantidad de intentos agotada")
#         intentos = 4
#     else:        
#         print(f"Ingreso {intentos} incorrecto, ingrese nuevamente la clave. \n Al intento 3 se bloqueará")
#         intentos +=1

#crear un programa que adivine una palabra secreta

# import random
# intentos = 5
# turno = 0
# ingreso = ""

# palabras_secretas = ["arroz", "fideo", "gato","perro"]
# adivina = random.choice(palabras_secretas)
# # print(adivina)
# while adivina  != ingreso and turno < intentos:
#     ingreso = input("Ingrese la palabra: ")
#     turno += 1
#     if ingreso == adivina:
#         print(f"Acertaste en el intento {turno}")
#     elif turno == intentos:
#             print(f"Se terminaron los intentos. La palabra es * {adivina} *\nSuerte en el próximo juego!!")
#     else:
#         print(f"Aun no acertaste. Sigue probando. vas en el intento {turno}")

# 
#--------------------ejercicio---------------
#se requiere encontrar el primer numero par en la lista usando un bucle while

# lista = [3,5,2,8,1,10]
# i=0
# while i < len(lista):
#     if lista[i] %2 == 0:
#         print("el primer numero par es", lista[i])
#         break
#     i += 1
# else:
# #no siempre el else está a la altura del if... 
#     print("No se encontró un número que sea par")
        
#calcular la suma de todos los numeros usando ciclo while 

numeros = [3,5,2,8,1,10]
i=0
suma=0
while i < len(numeros):
    suma = suma + numeros[i]
    i+=1
    
print(f"La suma de los números es: {suma}")    