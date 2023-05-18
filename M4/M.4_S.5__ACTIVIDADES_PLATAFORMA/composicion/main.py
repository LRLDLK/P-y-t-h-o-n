# from modelo.persona import Persona
# from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService
from modelo.supervisor_zona import SupervisorZona
from modelo.supervisor import Supervisor
from modelo.capacidades import Capacidades


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


    supervisor = Supervisor('Josua', 'Feliz', '3434', 'digital')
    capacidades = Capacidades('3','4')
    supervisor_zona = SupervisorZona(supervisor, capacidades)
    print(supervisor_zona.supervisor.area)
    print(supervisor_zona.capacidades.ncertificados)
    
    
    
    capacidades_2 = Capacidades('2','3')
    supervisor_zona.capacidades = capacidades_2
    print(supervisor_zona.capacidades.ncertificados)
    