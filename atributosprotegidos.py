class P:
    def __init__(self, x):
        #self._x Por regra pelos programadores voce ve isso como privado
        self.__x = x


obj = P(10)
#obj.__x não dá pra acessar
print(obj._P__x) # Dá pra acessar


