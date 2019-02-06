import heapq

class FilaDePrioridade:
	
	def __init__(self): # Construtor
		self.fila = []
		self.indice = 0
		
	
	def push(self, item, prioridade): # Conhecida por inserir
		heapq.heappush(self.fila, (-prioridade, self.indice, item))
	
	
	def pop(self): # REMOVER
		return heapq.heappop(self.fila)[-1] #Ele vai remover o último elemento
	
	
class Item:
	def __init__(self, nome):
		self.nome = nome
		
	def __repr__(self):
		return self.nome
	

fila = FilaDePrioridade()
fila.push(Item('Marcos'), 28)
fila.push(Item('João'), 30)
fila.push(Item('Maria'), 18)
print(fila.pop())
print(fila.pop())
