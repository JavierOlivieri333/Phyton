class volumen:
    def  __init__(self, base, altura, ancho):
        self.base=base
        self.altura=altura
        self.ancho=ancho
        
    def Rvolumen(self):
        return self.base*self.altura*self.ancho

print("FORMULA PARA EL VOLUMEN  ")
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
ancho=float(input("Ingrese el ancho: "))

#instamciamos la clase
algo=volumen(base,altura,ancho)
print("El resultado del volumen es: ", algo.Rvolumen(),"m3")