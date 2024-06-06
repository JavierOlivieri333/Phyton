from figurasgeometricas import FigurasGeometricas
from color import Color
class Cuadrado(FigurasGeometricas, Color):
    def __init__(self, lado, color):
    #super() respeta el orden de las clases definidas
        FigurasGeometricas.__init__(self, lado , lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.get_alto() * self.get_alto()
    
    def __str__(self):
        return "alto: " + str(self.get_alto()) + "alto: " + str(self.get_alto())
        