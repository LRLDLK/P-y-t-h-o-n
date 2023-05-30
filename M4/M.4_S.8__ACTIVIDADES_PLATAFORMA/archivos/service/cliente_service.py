from modelo.cliente import Cliente

class ClienteService:
    #constructor
    def __init__(self) -> None:
        # ClienteService tiene una lista de clientes como atributos para que la lista persista en la ejecucion
        self._clientes = self.load_clientes() #se carga la lista de clientes cuando se instancia ClienteService
    
    #carga de archivo, lectura y creación si el archivo no existe
    def load_clientes(self):
        try:
            with open('clientes.txt','r') as file: #apertura y cierra el archivo, se puede establecer el tipo de apertura
                clientes = file.readlines() #retorna una lista de tipo str con todas las lineas existentes            
        except FileNotFoundError: #si ocurre el error de archivo no existem se procede a crearlo
            #print('ERROR: error loading client')
            clientes = []
            with open('clientes.txt','w') as file:
                file.writelines(clientes) #crear el archivo si no existe, w es para escribir
        return clientes
    
    # Guardado de un archivo, escritura sobre el archivo
    def save_clientes(self):
        with open('clientes.txt','w') as file:
            for cliente in self._clientes: #se recorre la lista existente de cientes
                file.write(str(cliente)) #se va escribiendo en el archivo cliente a cliente
        
    def crear_cliente(self):
        #(self,nombre, apellido, rut, descuento)
        nombre = input('Ingrese el nombre del cliente: ')
        apellido = input('Ingrese el  apellido del cliente: ')
        rut = input('Ingrese el rut del cliente: ')
        descuento = input(f'Ingrese el descuento del cliente: ')
        
        #instanciar un cliente
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f'Cliente creado: {cliente}')
        
        #agregar el cliente a la lista existente en ClienteService
        self._clientes.append(cliente)
        
        
        #guardar los clientes
        self.save_clientes()
        
    #metodo para listar los clientes en la lista existente en ClienteService
    def list_clientes(self):
        print('Lista de clientes: ')
        for cliente in self._clientes:
            print(cliente)
            
    #metodo para obtener un cliente por rut en la lista existente
    def get_client_by_rut(self,rut):
        for cliente in self._clientes: #recorriendo la lista de clientes existentes 
            if cliente.rut == rut: #se filtra el cliente por rut
                return cliente #retorna el cliente encontrado
        return None    # si no sucede lo que está dentro el for, retorna None
    
    #editar clientes
    def edit_client(self):
        rut = input('Ingrese el rut del cliente que se editará: ')
        for cliente in self._clientes:
            if cliente.rut == rut:
                print('Cliente encontrado: ')
                cliente.nombre = input('Ingrese nuevo nombre del cliente')
                cliente.apellido = input('Ingrese el nuevo apellido del cliente')
                cliente.descuento = input('Ingrese el nuevo descuento del cliente')
                # se guarda la lista de nuevo en el archivo
                self.save_clientes()
                print("Cliente editado con éxito")
                print(cliente)
        print('Cliente no encontrado')
# [
#     'Cliente(nombre=cliente1, apellido=cliente1, rut=11, descuento=0.1)',
#     'Cliente(nombre=cliente2, apellido=cliente2, rut=22, descuento=0.2)',
#]
            