#padrão mais utilizado 

'''
Baixo acoplamento

Criação de objeto independente da classe

Cliente nao precisa conhecer a classe que cria o objeto, apenas metodos e parametros

Reutilza objetos existentes

'''

# Simple Factory

#Crie objetos sem expor a logica de sua criação. 

from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        print('au au')

class Gato(Animal):
    def falar(self):
        print('Meau')

class Fabrica(object):
    def produzir_som(self, object_type):
        return eval(object_type)().falar()

if __name__ == '__main__':
    f = Fabrica()
    f.produzir_som('Gato')


