class Funcionario:
	
	def __init__(self, nome, salario, cpf, x):
		self.nome = nome
		self.salario = salario
		self.cpf = cpf
		self.__x = x # Para deixar o atributo privado coloca DOIS __
		
	
	def get_bonificacao(self):
		return self.salario * 0.20 + self.salario
		

class Gerente(Funcionario):
	
	def __init__(self, nome, salario, cpf, senha):
		super().__init__(nome, salario, cpf)
		self.senha = senha
		
	
	def get_bonificacao(self):
		return super().get_bonificacao() + 1000.00



g = Gerente('Andrezza', 3000.00, 3929942, 2, 33233)
print(g.nome, g.salario, g.cpf)
print(g.get_bonificacao())
print(g.senha)

