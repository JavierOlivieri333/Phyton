from cuadrado import Cuadrado
from rectangulo import RRectangulo

cuadrado1 = Cuadrado(4, "azul")
print(cuadrado1.area())
print(cuadrado1.get_color())

rectangulo1 = RRectangulo(4, 5, "verde")
print(rectangulo1.areaRecta())
print(rectangulo1.get_color())