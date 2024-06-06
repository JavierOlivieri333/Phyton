class Aritmetica:
    """clase Aritmentica , para realizar sumas resta div y multiplicacion"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def multiplicacion (self):
        return self.operando1 * self.operando2
    
    def divide (self):
        return self.operando1/self.operando2
    
    #se instancia la clase
algo = Aritmetica(2, 4)
print("El resultado es: ",algo.sumar())      
print("El resultado es: ",algo.resta())      
print("El resultado es: ",algo.multiplicacion())      
print("El resultado es: ",algo.divide())      

