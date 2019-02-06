"""Responsável por fazer a conexão com o banco """

import sqlite3

class Database:
    def __init__(self, name='bank.db'):
        self.name = name
        self.conexao = None

    def conectar(self):
        self.conexao = sqlite3.connect(self.name)
    
    def desconectar(self):
        try:
            self.conexao.close()
        except AttributeError:
            print("Ocorreu um erro ao desconectar do banco")
            

