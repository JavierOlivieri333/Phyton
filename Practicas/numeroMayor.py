# numero1=str(input('intruduzcca un número'))
# numero2=str(input('intruduzcca un número'))
# numero3=str(input('intruduzcca un número'))
numero1=input('intruduzcca un número')
numero2=input('intruduzcca un número')
numero3=input('intruduzcca un número')


numeros=[1,10,1]
maximo=max(numeros)
print(maximo)
'''proceso estructurado'''
if(numero1==numero2 and numero1==numero3 and numero2==numero3):
    print("todos los numero son iguales")
else:
    if(numero1>=numero2 and numero1>=numero3):
        print(numero1)
    elif(numero2>numero1 and numero2>numero3):
        print(numero2)
    else:
        print(numero3)