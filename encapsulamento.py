# Quando queremos restringir acesso a classe
'''
class P():
    def __init__(self, x):
        self.__x = x # ATRIBUTO PRIVADO

    def getX(self):
        return self.__x

    def setX(self, x):
        if x > 0:
            self.__x = x

p = P(10)
print(p.getX())
p.setX(1)
print(p.getX())
'''
# Essa maneira acima é a que normalmente é feito, maas em python é outra forma que sera representado abaixo. 

class P():

    def __init__(self, x):
        self.x = x

    @property
    def x(self): #metodo get
        return self.__x

    @x.setter
    def x(self, x): #metodo set
        if x > 0:
            self.__x = x


p = P(10)
print(p.x)
p.x = -1
print(p.x)