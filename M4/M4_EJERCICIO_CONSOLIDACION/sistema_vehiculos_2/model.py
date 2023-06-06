"""
****Parte 2:****
Diseñe el Diagrama de Clases para las exigencias antes mencionadas por parte del
cliente.
● Codifique en Python las clases previamente diseñadas.
● Agregue las siguientes instancias en el archivo principal.

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

Verificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular,
Carga, Bicicleta y Motocicleta. Obteniendo la siguiente salida:
Salida:
$ python main.py
Marca Ford, Modelo Fiesta, 4 ruedas 180 Km/h, 500 cc Puestos: 5
Marca Daft Trucks, Modelo G 38, 10 ruedas 120 Km/h, 1000 cc Carga:
20000 Kg
Marca Shimano, Modelo MT Ranger, 2 ruedas Tipo: Carrera
Marca MW, Modelo KS, 2 ruedas Tipo: Deportiva Motor: 2T, Cuadro: Doble
Viga, Nro Radios: 21
Verificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular,
Carga, Bicicleta y Motocicleta. Obteniendo la siguiente salida:
Motocicleta es instancia con relación a Vehículo: True
Motocicleta es instancia con relación a Automovil: False
Motocicleta es instancia con relación a Vehículo particular: False
Motocicleta es instancia con relación a Vehículo de Carga: False
Motocicleta es instancia con relación a Bicicleta: True
Motocicleta es instancia con relación a Motocicleta: True
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
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc)'
# **** Fin Parte 1:****

#****Parte 2:****
class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos) -> None:#constructor
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada) #invocando a los atributos de la superclase 
        self.numero_puestos = numero_puestos
    
    def __str__(self) -> str:
        return super().__str__() +  f'Puestos: {self.numero_puestos}'
    
        
class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga) -> None:#constructor
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada) #invocando a los atributos de la superclase 
        self.peso_carga = peso_carga

    def __str__(self) -> str:
        return super().__str__() + f'Carga: {self.peso_carga}Kg'
        
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo) -> None:#constructor
        super().__init__(marca, modelo, numero_ruedas) #invocando a los atributos de la superclase 
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}'
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, motor, cuadro, numero_radios,) -> None:#constructor
        super().__init__(marca, modelo, numero_ruedas, tipo) #invocando a los atributos de la superclase 
        self.numero_radios = numero_radios
        self.cuadro = cuadro
        self.motor = motor
    
    def __str__(self) -> str:
        return super().__str__() + f'Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.numero_radios})'
              

# for indice, item in enumerate(lista):
#     print(f'Datos del automóvil {indice+1}: {str(item)}')




particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","DobleViga", 21)

lista = [particular, carga, bicicleta, motocicleta]

print('''
    **************************
      Datos de los vehículos
    **************************
      ''')

for item in lista:
    print(f'{str(item)}')


#verificar instancias
#Verificando la relación que existe de la instancia motocicleta

# print('Motocicleta es instancia con relación a Particular: ', isinstance(motocicleta, Particular))
# print('Motocicleta es instancia con relación a Carga: ', isinstance(motocicleta, Carga))
# print('Motocicleta es instancia con relación a Bicicleta: ', isinstance(motocicleta, Bicicleta))
# print('Motocicleta es instancia con relación a Vehículo: ', isinstance(motocicleta, Vehiculo))
# print('Motocicleta es instancia con relación a Vehículo: ', isinstance(motocicleta, Motocicleta))
# for temp in lista:
#     if isinstance(temp, Bicicleta):
      
# Verificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular,
# Carga, Bicicleta y Motocicleta. Obteniendo la siguiente salida:  
# Motocicleta es instancia con relación a Vehículo: True
# Motocicleta es instancia con relación a Automovil: False
# Motocicleta es instancia con relación a Vehículo particular: False
# Motocicleta es instancia con relación a Vehículo de Carga: False
# Motocicleta es instancia con relación a Bicicleta: True
# Motocicleta es instancia con relación a Motocicleta: True

tipo_auto = [Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta]
print('''
    **********************************
      Verificación de las instancias
    **********************************
      ''')
for tipo in tipo_auto:
    if tipo == Particular:
        print(f'Motocicleta es instancia con relación a Vehículo {tipo.__name__}: {isinstance(motocicleta, tipo)}')
    elif tipo == Carga:
        print(f'Motocicleta es instancia con relación a Vehículo de {tipo.__name__}: {isinstance(motocicleta, tipo)}')
    else:
        print(f'Motocicleta es instancia con relación a {tipo.__name__}: {isinstance(motocicleta, tipo)}')