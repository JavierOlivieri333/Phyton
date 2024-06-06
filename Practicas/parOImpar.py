#leyenda para q el usuario ingrese un numero y saber si par o no
print("Escriba un numero y dire si es par o impar")
# el usuario ingresa un texto 
usuario=input()
#lo convierto a numero
usuario=int(usuario)
#con un IF haciendo la cuenta modulo de 2 y el resultado es 0 se que par
if (usuario%2)==0:
    #imprimo en pantalla 
    print("Su numero es PAR")
    #sino
else:
    #imprimo en pantalla 
    print("Su numero es IMPAR")
