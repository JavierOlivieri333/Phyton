def esBisiesto(ano):
    if (ano % 4 ==0):
        if (ano % 100 == 0):
            if (ano % 400 == 0):
                return True
            else:
                return False
        else: 
            return True
    else:
        return False
pregunta=""
while pregunta=="":
    ano=int(input("ingrese un año para saber si este es BISIESTO\n"))

    print("si el ",ano ," %4==0 es BISIESTO\n",ano, "% 4 =", ano%4)
    print("si el ",ano ," %4==0 y ",ano," %100==0 NOOOO es bisiesto\n",ano, "% 100=",ano%100)
    print("si el ",ano ," %4==0 y ",ano," %100==0 y ", ano, " % 400 ==0 ahora si es BISIESTO \n",ano, "% 400=",ano%400)

    if esBisiesto(ano):
        print("AÑO BISIESTO")
    else:
        print("NO ES BISIESTO")

    pregunta=str(input("Enter para volver a preguntas"))
else:
    print("Programa finalizado")