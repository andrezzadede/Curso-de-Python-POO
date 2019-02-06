
# caso o programa use muita memoria criando muitas instancias

class Pessoa:
    __slots__ = ['nome', 'idade', 'peso']
    #Quando se usa isso, ele nao faz um dicionario, ele faz um array com o tamanho especifico, no entanto, não será possivel adicionar novos atributos
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
