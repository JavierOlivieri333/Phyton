print("proporcione lis siguientes datos")
print("-----------------------------")
nombre=input("Proporcione nombre: ")
id=int(input("Propocione un ID: "))
precio=float(input("Proporcione el precio: "))
envioGratis=int(input("Envio gratis 1 para si 2 para no (1-si/2-no)"))
if envioGratis==1:
    envioGratis="Envio gratis"
elif envioGratis==2:
    envioGratis="Sin envio gratis \n"
else:
    envioGratis ="Vuelva a introducir un dato correcto"    
    
print("el nombre del libro es: ", nombre)
print("el ID del libro: ", id)
print("el precio del libro: ", precio)
print("envio: ", envioGratis)
print(type(envioGratis))