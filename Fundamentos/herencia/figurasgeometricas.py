class FigurasGeometricas:
    def __init__(self, alto , ancho):
        self.__alto=alto
        self.__ancho=ancho
        
    def get_alto(self):
        return self.__alto
    
    def set_alto (self, alto):
        self.__alto=alto
        
    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self, ancho):
        self.__ancho=ancho
        
    def __str__(self):
        return "ancho: " + str(self.__ancho) + "alto" + str(self.__alto)