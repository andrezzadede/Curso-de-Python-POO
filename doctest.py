# Doctest biblioteca para executação de testes automatizados, escrever um tutorial ou docmentaçoes das classes dando exemplos de entrada e saida, ou seja como usar a classe. 

import doctest

class fib():

    def calculo_fib(self, n):
        """"
        Método para calcular o fibonacci

        >>> fib().calculo_fib(10)
        55

        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

if __name__ == '__main__':
    doctest.testmod(extraglobs={'f':fib()})




