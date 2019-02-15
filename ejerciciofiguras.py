class Shape():
    def __init__(self):
      pass

    def calcula_area(self):
        return
    def calcula_perimetro(self):
        return

class Cuadrado(Shape):
    def __init__(self, lado):
        self.lado = lado
        super().__init__()

    def calcula_perimetro(self):
        perimetro = self.lado *4
        return perimetro

    def calcula_area(self):
        area = self.lado **2
        return area

c = Cuadrado(4)
print(c.calcula_area())
print(c.calcula_perimetro())
