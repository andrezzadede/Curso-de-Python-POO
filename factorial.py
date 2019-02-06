from math import factorial

def meu_decorator(fat):
    def fat(x):
        return factorial(x)
    return fat
    

@meu_decorator
def dobro(x):
    return 2 * x