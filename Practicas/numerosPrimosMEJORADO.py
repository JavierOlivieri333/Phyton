#Notificacion para el usuario
print("Ver si un numero o no")
print("RECUERDEN")
print("Un numero es primo si es MAYOR A 1")
print("y divisible por 1 y si mismo y el resto es 0 ej. 7, 5, 3  ")
#ingreso un numero y lo convierto
numero=int(input("Ingrese un numero: "))
#si el numero es mayor a 1  
if numero >1:
    #for para compara con TODO los numero 
    for i in range (2, numero):
        #prueba si da resto 0 , entonces no es primo
        if (numero %i)==0:
            #imprimo resultado
            print(str(numero)+" no es un numero primo")
            #rompo el ciclo y salgo
            break
        else:
            #sino muestro todos los numero con los q se intento
            print("se probo con ",i, "")
else:
    #sino se rompio el I es primo y imprimo resultado
    print(numero, "es numero primo")
     