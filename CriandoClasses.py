class MinhaClasse:
	pass

# OU

class _MinhaClasse:
	pass # indica que não precisa fazer mais nada

#Ou seja, pode usar __

obj = MinhaClasse()

print(type(obj))

class P:
	pass

p = P()

p.x = 5
p.y = 30
p.nome = 'python'
print(p.x)
print(p.nome)

class Ponto:
	def resetar(self):
		self.x = 0
		self.y = 0
		
p = Ponto()
p.resetar()
print(p.x, p.y)

class Pontu:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def resete(self):
		self.x = 0
		self.y = 0
		
	def mover(self, x = 0, y = 0):
		self.x = x
		self.y = y
		
	#def algo(): ISSO NÃO PODE OCORRER, É NECESSARIO COLOCAR O SELF
	#	pass



'''
p1 = Pontu(10, 20)
print(p1.x, p1.y)
p1.resete() # Alternativa 1
print(p1.x, p1.y)
'''

p1 = Pontu(20, 20)
print(p1.x, p1.y)
Pontu.resete(p1) # Alternativa 2
print(p1.x, p1.y)
p1.mover(20, 32)
print(p1.x, p1.y)




