class TransacaoInvalida(Exception):
    pass

#raise TransacaoInvalida('Você não tem dinheiro')

class Transacao(Exception):
    def __init__(self, saldo_atual, quantidade):
        super().__init__('sua conta não tem R${}'.format(quantidade))
        self.quantidade = quantidade
        self.saldo_atual = saldo_atual
    
    def excesso(self):
        return self.quantidade - self.saldo_atual


try:
    raise Transacao(10, 20)
except Transacao as e:
    print(f'Voce não tem saldo babaca, R${e.excesso()}')