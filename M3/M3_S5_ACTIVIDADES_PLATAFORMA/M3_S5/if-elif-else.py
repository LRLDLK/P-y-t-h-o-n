#-------------------------
#estructuras condicionales
#-------------------------
#para evaluar cierta condicion declarada a varias
#if(condicion), donde condicion siempre es True, al menos no se cambie o modifique

numero=int(input("Ingrese un número entero: "))

if(numero>0):
    print(f"El numero {numero} es positivo (mayor a cero)")
elif(numero ==0):
     print(f"El numero {numero} es igual a cero)")
else:
    print(f"El numero{numero} es negativo (menor a 0)")    

print("-----------------------------------")
