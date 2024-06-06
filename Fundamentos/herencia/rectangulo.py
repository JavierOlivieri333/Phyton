from color import Color
from figurasgeometricas import FigurasGeometricas

class RRectangulo(FigurasGeometricas, Color):
    def __init__(self, alto, ancho, color):
        FigurasGeometricas.__init__(self, alto, ancho)
        Color.__init__(self,color)
        
    def areaRecta(self):
        return self.get_alto() * self.get_ancho()
    
    def __str__(self):
        return "ancho: " + str(self.get_ancho()) + "alto: " + str(self.get_alto())        
    