#Notificacion para el usuario
print("Ver si un numero o no")
print("RECUERDEN")
print("Un numero es primo si es MAYOR A 1")
print("y divisible por 1 y si mismo y el resto es 0 ej. 7, 5, 3  ")
#ingreso un numero y lo convierto
numero=int(input("Ingrese un numero: "))
#si el numero es mayor a 1  
if numero >1:
    #inicializo variable
    contador=0
    i=2
    #for para compara con TODO los numero 
    for j in range (2, numero):
        #comparo con el numero MIENTRAS q i sea menor  y contador sea mayor a 0
        while i<numero and contador==0:
            # creo una varibale y hago MODULO  de numero % de i
            resto=numero%i
            #si el resto el 0
            if resto==0:
                #contador=contador+1
                #sumo 1 al contador para saber que no es primo, ya q se divido por 2 hasta 1 antes del numero
                contador+=1
            else:
                #imprimo para ver con que numero se probo(es mas vistoso)   
                print("Se probo con "+str(i))
            #sumo 1 al contador del while
            i+=1
        
#resto 1 a la i para saber en q numero ya no es PRIMO        
i=i-1
#fuero del FON y MIENTRAS pregunto si el numero es primo
if contador==0:
    print("Si el "+str(numero)+" es un numeros primo")
else:    
    print("numeros no primo, el numero "+str(numero))
    print("Es divisible por "+str(i))