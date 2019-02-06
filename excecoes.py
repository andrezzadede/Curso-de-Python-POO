class SomentePares(list):

    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError('Somente inteiros') # raise lança uma exceção
        if inteiro % 2:
            raise ValueError('Somente Pares')
        
        super().append(inteiro)

sp = SomentePares()
sp.append(10)

# Efeitos de uma exceção
#Ela serve pra parar o programa

def algo():
    print('POO com Python')
    # Por exemplo, posso fazer um if e se aquele if for verdadeiro, eu coloco a exceção
    raise Exception ('Lançando excecao')
    print('Depois da exceção')
    return 'sucesso!'

# Se tiver uma função dentro da outra, e na segunda função ter uma exceção e ela for ativada, o resto da primeira função não será executado

# COMO REAGIR A EXCEÇÕES

# geralmente se utiliza o try... excepet

def algo2():
    raise Exception('excecao')

try:
    algo2()
except:
    print('Eu peguei uma exceção')
    print('excutado apos uma exceção')

    # Nesse codigo acima ele pega qualquer tipo de exceção
'''
def divisao(divisor):
    try:
        if divisor == 13:
            raise ValueError('13 Não é legal!')
        return 10 / divisor
    except ZeroDivisionError:
        return 'Divisao por zero'
    except TypeError:
        return 'Entre com um valor numerico'
    except ValueError:
        print('Não utilize o numero 13')
        else:
            print('Nenhuma exceção ocorreu')
        raise

print(divisao(13))
'''

try:
    raise ValueError('alguma coisa')
except ValueError as e:
    print('Os argumentos da exceção foram', e.args)
finally:
    print('Isso sempre será executado')

#Hierarquia de exceções

# Quando utiliza except ela vai pegar todas as exceções que ocorrer

