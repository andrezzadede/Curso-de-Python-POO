class Pessoa:

    def __init__(self, nome):
        self.nome = nome
    
    #Construtor alternativo
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)
    


p = Pessoa('Andrezza')
print(p.nome)

p1 = Pessoa.outro_construtor('Dede')
print(p1.nome)