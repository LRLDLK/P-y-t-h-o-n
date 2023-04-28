#------------
#cliclo while
#------------

# while(condicion)
#condicion siempre se evalua True al menos se cambie

# i=0
# while i<= 5:
#     i+=1 #contador
#     print(f"Imprimiento el valor de i {i}")
    
# i=0
# while i<= 5:
#     i+=1 #contador
#     if i==1:
#         continue
#     print(f"Imprimiendo el valor de i {i} y probando continue")
        
# i=0
# while i<= 5:
#     i+=1 #contador
#     if i==4:
#         break
#     print(f"Imprimiendo el valor de i {i} y probando break")
    
#romper un ciclo infinito, con precaucion
# while True:
#     print("Palabra")
#     break

#ciclos while
#pensar cual es la condicion que hara que el ciclo termine para que no sea infinito
"""
imprimir valores del 1 al 5
"""

i=1
while i <= 5:
    print(i)
    i +=1
    
j=1
while j <= 5:
    print(j)
    j +=1
    
    while True:
        print("imprime hasta que")
        break #terminae el ciclo