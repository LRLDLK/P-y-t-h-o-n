"""
****Parte 3:****
En esta tercera parte el cliente quiere que se guarden los datos en un archivo con el nombre de
vehiculos.csv, es decir, un archivo separado por comas.

● Crear el método que permita guardar cada uno de los objetos previamente creados en el
archivo vehiculos.csv, el nombre del método es: guardar_datos_csv(self)

La estructura para guardar son la clase, y luego los atributos del objeto de la clase.
● Cree un método que lea del archivo vehiculos.csv con el nombre leer_datos_csv(self) y
que imprima por pantalla o terminal lo siguiente según la clasificación del vehículo:

$ python main.py
Lista de Vehiculos Particular
{'marca': 'Ford', 'modelo': 'Fiesta', 'nro_ruedas': '4', 'velocidad':
'180', 'cilindrada': '500', 'nro_puestos': '5'}
Lista de Vehiculos Carga
{'marca': 'Daft Trucks', 'modelo': 'G 38', 'nro_ruedas': '10',
'velocidad': '120', 'cilindrada': '1000', 'carga': '20000'}
Lista de Vehiculos Bicicleta
{'marca': 'Shimano', 'modelo': 'MT Ranger', 'nro_ruedas': 2, 'tipo':
'Carrera'}
Lista de Vehiculos Motocicleta
{'marca': 'BMW', 'modelo': 'F800s', 'nro_ruedas': 2, 'tipo':
'Deportiva', 'motor': '2T', 'cuadro': 'Doble Viga', 'nro_radios': 21}
● En los métodos creados utilice el manejo de excepciones en caso de errores en el
archivo.
lines = [line for line in lines if line.strip()] 
"""
import csv


# ****Parte 1:****
class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
    
# ****Parte 3:****
    def guardar_datos_csv(self, nombre_archivo):
        try:
            archivo = open(nombre_archivo, "a+", newline='') #se abre el archivo
            datos = [(self.__class__.__name__, self.__dict__)] #se crea lista con tupla interna
            archivo_csv = csv.writer(archivo)#apertura la escritura del archivo
            archivo_csv.writerows(datos) #se escribe dentro del archivo
            archivo.close() #se cierra el archivo
        except FileNotFoundError: #por si el archivo no existe
                print('ERROR: Archivo no encontrado', nombre_archivo)
                # with open(nombre_archivo,'w'): #forma de crear
                #     print('Archivo creado')
        except Exception as e:
                print('ERROR: ',  e)    
        
    def leer_datos_csv(self, nombre_archivo): 
        try:
            vehiculos = [] # lista para agregar los datos o lineas leidas desde el archivo, en cada posicion de la lista
            archivo = open(nombre_archivo, "r") # r, se abre el archivo como escritura
            archivo_csv = csv.reader(archivo) # se recorre la lista obtenida de la lectura
            for vehiculo in archivo_csv: # se agrega el objeto temporal vehiculo dentro de la lista con .append()
                vehiculo
                vehiculos.append(vehiculo) #se cierra el archivo
            archivo.close()
            return vehiculos
        except FileNotFoundError: #archivo no existe
            print('ERROR: file not found ', nombre_archivo)
        except Exception as e:
            print("ERROR: ",e)

#**** Fin Parte 3:**** 
   
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
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Puestos: {self.numero_puestos}'
            

        
class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga) -> None:#constructor
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada) #invocando a los atributos de la superclase 
        self.peso_carga = peso_carga

    def __str__(self) -> str:
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Carga: {self.peso_carga}Kg'
        
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
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.numero_radios})'
              


particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","DobleViga", 21)

# **** Fin Parte 2:****


#****Parte 3:****

particular.guardar_datos_csv('vehiculos.csv')
carga.guardar_datos_csv('vehiculos.csv')
motocicleta.guardar_datos_csv('vehiculos.csv')
bicicleta.guardar_datos_csv('vehiculos.csv')

listado = []
print(('--------------- LISTADO según clasificación ---------------').upper())
listado.append(particular.leer_datos_csv('vehiculos.csv'))

for item in (listado):
    for it in (item):
        print(f'Lista de Vehículos {str(it[0])} \n {str(it[1])}')
 