"""
****Parte 1:****
● Diseñe el diagrama de clases según los datos capturados con el cliente.
● Partiendo del diseño de diagrama de clases previamente construido, diseñe en las Clases
en Python.
● Genere tres instancias, y al ejecutar el programa se debe mostrar lo siguiente:

    #Datos del automóvil 1 : Marca Toyota, Modelo Yaris, 4 ruedas, 120 Km/h, 800 cc
    #Datos del automóvil 2 : Marca Fiat, Modelo Palio, 4 ruedas, 95 Km/h, 1200 cc
    #Datos del automóvil 3 : Marca Ford, Modelo Fiesta, 4 ruedas, 125 Km/h, 1500 cc
"""

# ****Parte 1:****
class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada) -> None:#constructor
        super().__init__(marca, modelo, numero_ruedas) #invocando a los atributos de la superclase 
        self.velocidad = velocidad
        self.cilindrada = cilindrada    
       
    def __str__(self) -> str:
        return f'Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc'
              
def crear_automovil():
    marca = input('Ingrese Marca del vehículo: ')
    modelo = input('Ingrese el Modelo del vehículo: ')
    nro_ruedas = input('Ingrese la cantidad de ruedas del vehículo: ')
    velocidad = input('Ingrese la velocidad del vehículo: ')
    cilindrada = input('Ingrese la cilindrada del vehículo: ')
    return Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
   
   
while True:
    try:
        ingreso = int(input('Cantidad de automóviles a crear: '))
        break
    except ValueError:
        print('ERROR: debe ser número entero, ingrese Cantidad nuevamente')
    except Exception as e:
        print('ERROR: ', e)        

lista = []

for i in range(1, ingreso+1):
    auto = crear_automovil()
    lista.append(auto)
    print (f"--------------------------\nAutomóvil: {i} ha sido creado\nDatos del automóvil: {str(auto)}\n--------------------------")

# for indice, item in enumerate(lista):
#     print(f'Datos del automóvil {indice+1}: {str(item)}')

print('''
    ***********************
      Automóviles Creados
    ***********************
      ''')
indice = 1
for item in lista:
    print(f'Datos del automóvil {indice}: {str(item)}')
    indice +=1
    
print('***********************')
# **** Fin Parte 1:****

