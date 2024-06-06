#importo la biblote del numero aleatorio'
import random
#inicio las variables
intentos=0
NumMinimo=1
NumMax=99
jugador=-1
# inicio la variable numero con un rando entre el numero minimo y el maximo
numero=random.randint(NumMinimo,NumMax)
print("Adivina el numero en q estoy pensando")
#entro en el while y salgo presionando la tecla 0 y enter
while jugador!=0:
    # digo q escriba un numero entre numero de la variable  NumMinimo y NumMax
    print("Escriba un numero entre el "+str(NumMinimo)+" al "+str(NumMax)+", a ver si adivina , para salir esciba el 0")
    #el usuario ingresa un numero
    jugador=input()
    #lo convierto el texto en numero 
    jugador=int(jugador)
    #CONTADOR para sumar los intento
    intentos=intentos+1
    # IF para ver si es mayor menor 
    if (jugador < numero):
        print("NO, el numero en el que pienso es mayor, para salir esciba el 0")
    elif(jugador>numero):
        print("NO, el numero en el que pienso es menor, para salir esciba el 0")
    #else(jugador==numero): esto no ES ASI en python
        #salgo del while si gano
    else:
        #leyenda si gano y convierto la variable numerica en STRING
        print("FELICITACION GANO, en "+ str(intentos) + " intentos")
        break 
        
#salgo del while rompiendo la identaion
#terminado el juego muestro el numero q la maquina penso , lo convierto en string y lo muestro
print("El numero en que pensaba era "+str(numero))

#leyenda para saber q sali del programa
print("Ah salido del juego")
