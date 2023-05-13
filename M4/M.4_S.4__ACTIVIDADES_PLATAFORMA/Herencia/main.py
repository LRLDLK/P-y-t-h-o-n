from modelo.persona import Persona
from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService


def main():
    #creando instancias para porder acceder a service
    menu_service = MenuService()
    cliente_service = ClienteService()
    supervisor_service = SupervisorService()
    
    while True:
        menu_service.imprimir_menu()
        opcion = input("Ingrese una opcipión: ")
        match opcion: 
            case "1":
                cliente_service.crear_cliente()
            case "2":
                supervisor_service.crear_supervisor()
            case "3":
                break
            case _:
                "Opción inválida. Saliendo del programa"

#funcion inicializadora para dar un punto de entrada/inicio al programa                
if  __name__ == "__main__":
    main()
    
    
    
    
    
    
    

#pruebas:
# persona = Persona("fulano", "perez", "123456789")
# print(persona)
# print(str(persona))
# persona.get_tipo()

# print("-------------------------")

# cliente = Cliente("fulano", "perez", "123456789", "0.1")
# print(cliente)
# print(str(cliente))
# cliente.get_tipo()
