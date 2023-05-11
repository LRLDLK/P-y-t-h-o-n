class Vehiculo:
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0
        self.encendido = False

#getter and setters son funciones para obtener o dar valor a los atributos:

#getters
    def get_marca(self):
        return self.marca

    def get_color(self):
        return self.color
    
    def get_modelo(self):
        return self.modelo

  

#setters
    def set_marca(self,marca):
        self.marca = marca

    def set_color(self,color):
        self.color = color

    def set_modelo(self,modelo):
        self.modelo = modelo




#funciones que realiza el objeto accediendo da traves de la instancia
    def arrancar(self):
        if self.encendido:
            return(f"Vehículo de marca {self.marca} ya se encuentra en encendido, no se puede volver a arrancar")
        else:        
            self.encendido = True
            self.velocidad = 10
            return(f"Vehículo de marca {self.marca} está en encendido a una velocidad {self.velocidad}")
        
    def frenar(self):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= 10
            return f"Vehículo de marca {self.marca} y {self.modelo} está frenando"
        else:
            return f"Vehículo de marca {self.marca} y módelo {self.modelo} ya está detenido"
        
    def girar_izquierda(self):
        if self.encendido:
            return f"Vehículo de marca {self.marca} está girando a la izquierda"
        else:
            return f"Vehículo de marca {self.marca} debe estar en encendido"

    def girar_derecha(self):
        if self.encendido:
            return f"Vehículo de marca {self.marca} está girando a la derecha"
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return f"Vehículo de marca {self.marca} se ha apagado"
        else:
            return f"Vehículo de marca {self.marca} ya está apagado"
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"Vehículo de marca {self.marca} ha sido encendido"
        else:
            return f"Vehículo de marca {self.marca} ya está encendido"
        
    def acelerar(self):
        if self.encendido:
            self.velocidad += 10
            return f"Vehículo de marca {self.marca} ha aumentado su velocidad en 10 y está en {self.velocidad}"
        else:
            return f"Vehículo de marca {self.marca} no puede acelerar, no se encuentra encendido"

    def retroceder(self):
        if self.encendido:
            self.velocidad -= 10
            return f"Vehículo de marca {self.marca} está retrocediendo"
        else:
            return f"Vehículo de marca {self.marca} no puede retroceder porque no está encendido"

#instanciar vehículos para realizar las acciones mediante funciones
mazda = Vehiculo("Mazda","Blanco","M4",2000,2.5,2)
toyota = Vehiculo("Toyota","Negro","Yaris",1500,1.5,1)

#cambiar el comportamiento mendiante las funciones, accediendo desde la instancia de las funciones
print(mazda.arrancar())
print(mazda.acelerar())
print(mazda.encender())
print(mazda.apagar())
print("_________________")
print(toyota.encender())
print(toyota.encender())
print(toyota.arrancar())
print(toyota.acelerar())
print(toyota.frenar())
print("_________________")

#get (obtener) el valor del atributo a traves de notacion de puntos
print(mazda.color)
print(mazda.get_color())

#setear (cambiar) valor a traves de notacion de puntos
mazda.color ="Azul"
print(mazda.get_color())
mazda.set_color("Rosado")

print(mazda.get_color())