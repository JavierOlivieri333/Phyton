def promedio():
    resptuesta='s'
    contador=0
    acumulador=0
    while resptuesta!='n':
        try:
            monto=float(input('ingrese su monto: '))
            contador+=1
            acumulador=acumulador+monto
            resptuesta=input('continua: ')
        except ValueError:
            # while monto is numeric(chr[, default])
            print('El monto debe ser en numeros')
    print('promedio', acumulador/contador, 'acumulador', acumulador, 'contador', contador)
promedio()


    