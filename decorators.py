'''
Decorator = Função que recebe outra função como parametro, gera uma nova função que adiciona algumas funcionalidades à função original e a retorna essa nova funçao
'''

'''
def modificar(funcao):
    def subtrair(a, b):
        return a - b
    return subtrair

@modificar
def soma(a, b):
    return a + b

print(soma(2, 4))
'''

def modificar(funcao):
    def somar_pares(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return a - b
    return somar_pares

@modificar
def soma(a, b):
    return a + b

print(soma(2, 2))


def meu_decorador(funcao):
    def imprime_algo():
        print('Eu não sei somar')
    return imprime_algo

@meu_decorador
def imprime():
    print('Eu sei somar')

imprime()