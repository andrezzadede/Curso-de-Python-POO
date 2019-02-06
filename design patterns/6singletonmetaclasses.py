#Singleton e Metaclasse

#Metaclasse é a classe de outra classe, ou seja, a classe é uma instancia de sua meta classe. 

# Definição de classe é determinar pela sua meta classe

#Exemplo a = 10, type(a)=int type(int) = type

class MetaSingleton(type):
    _instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Test(metaclass=MetaSingleton):
	pass

t1 = Test()
t2 = Test()
print(t1, t2)