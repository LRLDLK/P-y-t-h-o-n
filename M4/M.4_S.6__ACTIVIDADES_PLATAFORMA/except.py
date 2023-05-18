"""
Las excepciones pueden ocurrir en el momento de transformacion, asignacion,
evaluacion de variables o atributos.
Las excepciones ocurren con errores de ejecucion
Comunicando con entes externos al proyecto
Class Exception es la clase orbcuoa de todas las excepciones que ocurran en la logica
"""
def division():
    try:
        num1 = 10
        num2 = 0
        res = num1/num2
        print(res)
    except ZeroDivisionError as e:
        print("ERROR: no válido -> ",e)
    
    except Exception as error:
        print(f'ERROR: {error}')
        
        
def division_ingreso():
    try:
        num1 = int(input('ingrese un numero entero: '))
        num2 = int(input('ingrese un numero entero: '))
        res = num1/num2
        print(res)
    except Exception as e:
        print("ERROR: no válido -> ",e)       
        division_ingreso() #funcion con recursividad, cuidar para no crear bucle infinito
        
#division_ingreso() 
      
    
def ingreso():
    try:
        ingreso = int(input('ingrese un numero entero: '))
        print(f'El numero ingresado es: {ingreso}')
    except ValueError as e:
        print("ERROR: no válido -> ",e)
    
#crear excepcion propia, para ciertos casos 

#ejemplo 1:       
# class CustomException(Exception):
#     pass
#ejemplo 2:
class CustomException(Exception):
    def __init__(self, mensaje, codigo) -> None:
        super().__init__(mensaje) 
        self.codigo = codigo

def excepcion_propia():
    try:
        edad = int(input("Ingrese edad para manejar excepciones: "))
        if edad < 0:
            raise CustomException("Expecion propia ejecutada", 460)#levantar excepcion
        print(f'edad: {edad}')
    except ValueError:
        print(f'ERROR: ingreso inválido')
    except CustomException as e:
        print(f'ERROR: {e} y manejada -> ')
        print(f'ERROR: {e.codigo}')

excepcion_propia()