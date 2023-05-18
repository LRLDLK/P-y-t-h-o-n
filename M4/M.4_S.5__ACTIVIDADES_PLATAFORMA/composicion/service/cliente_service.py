from modelo.cliente import Cliente #importando la clase supervisor 

class ClienteService:
    def crear_cliente(self):
        nombre = input('Ingrese el nombre del cliente: ')
        apellido = input('Ingrese el  apellido del cliente: ')
        rut = input('Ingrese el rut del cliente: ')
        descuento = input('Ingrese el descuento del cliente: ')
        
        #para crear un cliente se realiza una instancia de un constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f"Cliente creado: {cliente}")