# Quando um método é chamado por outra classe e é utilizado de outra forma
import math
class Forma():

    def __init__(self): # Inicializador de instancia/ Construtor
        print('Construtor da forma')

    def area(self):
        print('Area da forma')

    def perimetro(self):
        print('Perimetro da forma')
    
    def descrição(self):
        print('Descrição da forma')

    
class Quadrado(Forma):
    # Forma é uma generalização de quadrado
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4

class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def descrição(self):
        return print('Descrição do circulo')
    


quad = Quadrado(2)
print(f'Area {quad.area()}')
print(quad.perimetro())
print('Circulo')

circulo = Circulo(3)
print(f'Area do Circulo: {circulo.area()}')
print(f'Perimetro do circulo: {circulo.perimetro()}')
print(circulo.descrição())




