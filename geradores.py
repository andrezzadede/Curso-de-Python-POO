#Geradores (Generators) Ele produz itens sem necessariamente acesar uma coleção
from symbol import yield_expr

#São funções que usam a YIELD

#Exemplos

def fib(max):
    x, y = 1, 1
    while x < max:
        yield x # A cada yield ele congela, ou seja, ele para apresenta resultado e não restaura a função, quando volta, ele continua onde parou
        x, y = y, x + y


gen = fib(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def gerar_numeros():
        yield 1
        yield 2
        yield 3

for v in gerar_numeros():
        print(v, end= ' ')

#OU

nosso_gerador = gerar_numeros()

print(next(nosso_gerador))
print(next(nosso_gerador))
print(next(nosso_gerador))

def is_prime(number):
    for i in range(3, number):
        if number % i == 0:
            return False
    return True
                


def get_primes(number):
        while True:
                if is_prime(number):
                        yield number
                number += 1

meu_gerador = get_primes(10)
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))