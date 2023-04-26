# calcular resistenacia de un circuito
# formula RT=1/((1/R1)+(1/R2)+(1/R3)+1(1/Rn))

# r1 = float(input("Ingrese la resistencia 1 : "))
# r2 = float(input("Ingrese la resistencia 2 : "))
# r3 = float(input("Ingrese la resistencia 3 : "))
# rT = (1/((1/r1)+(1/r2)+(1/r3)))

# print("La resistencia total es: {:.2f}".format(rT))

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

