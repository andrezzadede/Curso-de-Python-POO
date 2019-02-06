# Meta classe é a classe de uma classe, ela define como uma classe se comporta
#Meta classe é como se fosse a classe de fabrica, como o type

class MinhaMetaClasse(type): #Elas sempre vão herdar de TYPE
    def __new__(cls, clsname, superclasses, attributedict):
        print('clsname:', clsname)
        print('superclasses: ', superclasses)
        print('atributos: ', attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class Pai:
    pass

class Filha(Pai, metaclass=MinhaMetaClasse):
    pass

obj = Filha()
