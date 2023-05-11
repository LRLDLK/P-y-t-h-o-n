class Animal:
    def __init__(self,nombre,raza,edad,peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
    def comer(self):
        print(f"El animal {self.nombre} está comiendo")
 
    def caminar(self):
        print(f"El animal {self.raza} está caminando")

    def dormir(self):
        print(f"El animal {self.nombre} está durmiendo")
    
#definir una instancia de tipo Animal para un objeto llamado perro
perro = Animal("Brando","San Bernardo",3,30)

#definir una instancia de tipo Animal para un objeto llamado gato
gato = Animal("Roll","Persa",4,3)

perro.caminar()
perro.comer()
perro.dormir()

gato.caminar()
gato.comer()
gato.dormir()
