class rectangulo:
    #"""clase BxA de cuadrado"""

    def  __init__(self,base ,altura):
        self.base=base
        self.altura=altura
    
    def baseXaltura(self):
        return self.base*self.altura
    
print("Ingrese dato para un area del RECTANGULO")
base=int(input("Ingrese la base: "))
altura=int(input("Ingrese la altura: "))
algo1=rectangulo(base, altura)
print("El area de la base", base, "por la altura", altura, "es:", algo1.baseXaltura())