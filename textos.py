class Texto:
    def __init__(self, texto, color):
        self.texto = texto
        self.__color = color
    
    def imprimir(self):
        print(self.texto)
    
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color = color

class TextoHijo(Texto):
    def __init__(self, texto, color, tamano):
        super().__init__(texto,color)
        self.tamano = tamano
    
    def mostrar(self):
        print(self.tamano)
    
texto1= Texto('Hola mundo', 'rojo')
texto1.imprimir()

texto2 = TextoHijo('Adios mundo', 'negro', 12)
texto2.imprimir()
texto2.mostrar()