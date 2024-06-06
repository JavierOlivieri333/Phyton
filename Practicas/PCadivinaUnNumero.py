#importo la biblote del numero aleatorio'
import random
#inicio las variables
intentos=0
NumMinimo=1
NumMax=99
respuesta=-1
# inicio la variable numero con un rando entre el numero minimo y el maximo
print("La PC adivina en q numero piensas")
#entro en el while y salgo presionando la tecla 0 y enter
print("Escriba un numero entre el "+str(NumMinimo)+" al "+str(NumMax))
while respuesta!=3:
   #la PC elije un numero random entre las variable NumMinimo y NumMax
    numero=random.randint(NumMinimo,NumMax)
    #imprimo el numero por pantalla
    print("PC dice: ",numero)
    #imprimo elecciones para el usuario
    print("Elija:\nEs menor 1 \nEs mayor 2 \n3 GANASTE PC")
    respuesta=int(input("Ud dijo:"))
    #primero intente con el IF
    #if respuesta==1:
    #    NumMax=numero
    #elif respuesta==2:
    #    NumMinimo=numero
    #else:
    #    break
    
    #me gusto mas el switch (no hay necesidd de consumo por preguntas)
    match respuesta:
        case 1:
            NumMax=numero
        case 2:
            NumMinimo=numero
        case _:
            break
    #su iterados del MIENTRAS
    intentos+=1
print("La PC gano en ", intentos ," intentos")

    
  