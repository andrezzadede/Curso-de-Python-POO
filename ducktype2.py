#Duck Typing - Parte 2 - LBYL e EAFP

class Pato:
    def quack(self):
        print('Quack, quack')


class Pessoa:
    def quack(self):
        print('Eu faço quack igual a um pato')

'''
ISSO NAO É PYTONICO
def fazer_quack(obj):
    if isinstance(obj, Pato): #Se a instancia 
        obj.quack()
    else:
        print('Isso tem que ser um pato')
'''
'''
def fazer_quack(obj):
    #LBYL É um estilo de codificação que testa as pré condições antes de fazer chamadas
    if hasattr(obj, 'quack'): #verifica se tem esse objeto
        if callable(obj.quack): # se for chamavel
            obj.quack()

            NÃO É PYTONICO
'''
def fazer_quack(obj):
    # EAFP Easier to ask for forgiveness than permission
    #ESTILO COMUM EM PYTHON
    try:
        obj.quack()
    except AttributeError as e:
        print(e)
        

pato = Pato()
pato.quack()

pessoa = Pessoa()
pessoa.quack()

print('Função')

fazer_quack(pato)
fazer_quack(pessoa)