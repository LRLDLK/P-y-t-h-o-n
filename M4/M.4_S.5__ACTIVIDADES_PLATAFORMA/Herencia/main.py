# from modelo.persona import Persona
# from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService
from modelo.supervisor_zona import SupervisorZona


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
    #main()



    supervisor_zona = SupervisorZona('Maria', 'papa', '223', 'tech', '3', '9', '3')
    print(supervisor_zona.nombre)
    print(supervisor_zona.promedio)
    
    
    
    
    
    

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
