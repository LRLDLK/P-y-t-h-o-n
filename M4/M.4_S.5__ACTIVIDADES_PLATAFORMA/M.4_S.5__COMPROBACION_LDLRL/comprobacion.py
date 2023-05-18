"""
EJERCICIOS:
Para llevar a cabo esta actividad, comenzaremos con la base del siguiente código en Python:
1 class A:
2 def __init__(self):
3 print("Pertenezco a la clase A")
4 
5 def metodo_a(self):
6 print("Método heredado de A")
7
8 class B:
9 def __init__(self):
10 print("Clase B")
11 
def metodo_b(self):
print("Método heredado de B")
 
1. Construya una nueva clase C que tenga herencia múltiple de B y A respectivamente, y
que contenga el metodo_c que imprima por pantalla “Método de clase C”.
2. Cree un nuevo objeto C, y al instanciarlo y acceder a cada método: metodo_a, metodo_b
y metodo_c tenga como resultado lo siguiente:
1 Clase B
2 Método heredado de A
3 Método heredado de B
4 Método es de C
"""

# from multipledispatch import dispatch
class A:
    def __init__(self):
        print("Pertenezco a la clase A")
   
    def metodo_a(self):
        print("Método heredado de A")
        

class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")
        
class C(B,A):    
    def metodo_c(self):
        return("Método de clase C")
    
    #sobreescritura de metodo
    # def metodo_a(self):
    #       print("Método Sobreescrito A")

#invocando al constructor
#necesario para crear el objeto 
c = C() 


#Acceso estático o a traves del nombre de la clase
c.metodo_a()
c.metodo_b()
c.metodo_c()


print(isinstance(c, C))

