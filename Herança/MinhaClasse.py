class Minhaclasse(object):
	pass


class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
		
	
	
class PessoaFisica(Pessoa):
	def __init__(self, CPF, nome, idade):
		Pessoa.__init__(self, nome, idade)
		self.CPF = CPF
		

class PessoaJuridica(Pessoa):
	def __init__(self, CNPJ, nome, idade):
		Pessoa.__init__(self, nome, idade)
		self.CNPJ = CNPJ
		
		
p1 = Pessoa('Marcos', 32)
print(p1.nome)
print(p1.idade)

p_fisica = PessoaFisica(3232323, 'Andre', 31)
p_juridica = PessoaJuridica(323134, 'Leão', 5)

print(p_fisica.nome, p_fisica.idade, p_fisica.CPF)

print(p_juridica.nome, p_juridica.idade, p_juridica.CNPJ)
		
		
