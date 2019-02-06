from collections import namedtuple

Estoque = namedtuple('Estoque', 'x y z')

estoque = Estoque(10, 20, 30)

print(estoque.x)

#Isso funciona para dados de apenas leitura, pois são tuplas

## Dicionario

d = {'Marcos': 32, 'Anna': 32}
print(d)
print(d.get('Anna'))
# valores
print(d.values())
#Todos os itens
print(d.items())
#As chaves
print(d.keys())

for nome, idade in d.items():
    print(nome, idade)

#Dicionario não garante a ordem

class MyClass:
    def __init__(self, valor):
        self.valor = valor

obj = MyClass(20)
d = {}
d[obj] = 'Marcos'
obj2 = MyClass(28)
d[obj2] = 'Joao'

#Listas

#As listas serve para quando queremos inserir varias instanciaas de um mesmo objeto
#Elas podem ser modificadas, inseridas, deletadas

lista = [1,2,3,'Annie']
print(lista[-1])
print(lista[0:2])
lista.append(10)
print(lista)
print(lista.count('Annie'))

#Conjutos, nao permitem elementos reptidos, eles nao garantem a ordem

c = set()
c.add(10)
c.add(20)
c.add(10)
print(c)

# Caso eu queira acrescentar vários elementos em uma lissta por meio do append, no caso, ele só aceita um por vez, por issso dá para sobreescreve-lo
# Exemplo a baixo

class MinhaLista(list):
    def append(self, *args):
        self.extend(args)


l = MinhaLista()
l.append(1)
l.append(3, 2, 5, 3, 2)
print(l)

class MyList(list):
    def sort(self):
        return 'Opa! Você quer ordenar?'
