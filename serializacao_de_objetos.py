#Processo de tradução de objeto para ser salvo em um buffer de memoria

import pickle
import json

meus_dados = ['marcos', 3.21, [1,2,4]]

with open('arquivo.txt', 'wb') as file:
    pickle.dump(meus_dados, file)

with open('arquivo.txt', 'rb') as file:
    dados_carregados = pickle.load(file)

print(dados_carregados)

#JSON
#Serealizando objetos: Jason
class Contato():
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return(f'{self.primeiro_nome} {self.sobrenome}')


c = Contato('Marcos', 'Babuino')
print(json.dumps(c.__dict__))