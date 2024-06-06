#concatenacion
separador='-----------------\n'
var_hola='hola'
var_mundo='mundo'

print(var_hola, var_mundo) # el espacio lo hace solo
print(separador)

var_hola_mundo=var_hola + var_mundo
print(var_hola_mundo)
print(separador)
var_hola_mundo2=var_hola + ' ' + var_mundo
print(var_hola_mundo2)
print(separador)
#interpolacion (dar formato)
var_hola_mundo =f'mi nueva cadena es: {var_hola} {var_mundo}'
print(var_hola_mundo)
print(separador)
#interpolacion de varias lineas con formato
print(f'''Mi cadena nueva es:
{var_hola}
        {var_mundo}''')
