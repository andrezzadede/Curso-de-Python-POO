#import poligono
#from poligono import Quadrado
#from poligono import Retangulo

from Modulo.poligono import Quadrado, Retangulo
# Acima é caso o main esteja em uma pasta diferente

q = Quadrado(5)
print(q.perimetro())
print(q.area())

r = Retangulo(5, 10)
print(r.area())
