#--------
# ciclo
# -------

#ejecutan instrucciones repetitivas hasta que se cumpla una condicion, 
# se finalice el ciclo loop


#ciclo for
#----------
#for i in data:
#   instrucciones a realizar

frutas =["pera","kiwi","piña"]

for i in frutas:
    print(i)
    
#for i in range:
#   instrucciones a realizar
for i in range(1,6):
    print(i)
    
#conocemos los elementos
for i in range(len(frutas)):
    print(i)

#conocemos los elementos y la posicion
palabra = "python"
for i in range(len(palabra)):
    print(palabra[i])