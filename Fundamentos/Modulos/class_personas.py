class personas:
    def  __init__(self,nombre,edad):
        # el __ antes de una variable es q es PRIVADO
        self.__nombre=nombre
        self.__edad=edad
        
    def __str__(self) -> str:
        return "Nombre: " + self.__nombre + " edad: " + str(self.__edad)