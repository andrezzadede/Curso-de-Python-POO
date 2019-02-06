#Implementação do padrão Singleton

'''

Padrão de projeto Singleton
Garante que apenas um objeto da classe seja criado
Usado geralmente em banco de dados

'''

class Singleton(object):
    def __new__(cls): #Subscreveu o metodo new 
        if not hasattr(cls, 'instance'): # Verifica se o objeto já existe, hasattr verifica se já tem um objeto
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)

# Instanciação preguiçosa no Padrao Singleton

# Ela garante que o objeto vai ser criado quando realmente for usado o objeto

class Singleton1:
    __instance = None
    def __init__(self):
        if not Singleton1.__instance:
            print('__init__ foi chamado')
        else:
            print('instancia já criada: ', self.obter_instancia())
    @classmethod
    def obter_instancia(cls):
        if not cls.__instance:
            cls.__instance = Singleton1()
        return cls.__instance

s = Singleton1()
print('Objeto criado: ', Singleton1.obter_instancia())
s2 = Singleton1()

# Padrão Singleton Monostate

class MinhaClasse:
    __estado_compartilhado = {'1':2}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__estado_compartilhado 

b1 = MinhaClasse()
b2 = MinhaClasse()
b1.x = 5

print('b1:', b1)
print('b2:', b2)

print(b1.__dict__)
print(b2.__dict__)

