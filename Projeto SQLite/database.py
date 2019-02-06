#Criando a classe do banco SQLITE

import sqlite3

class BancoDeDados:
    '''
    Classe que representa o banco de dados da aplicação
    '''
    def __init__(self, nome='banco2.db'):
        self.nome = nome
        self.conexao = None

    def conecta(self):
        """ Conecta passando o nome do arquivo """
        self.conexao = sqlite3.connect(self.nome)
    
    def desconectar(self):
        """ Desconecta do banco """
        try:
            self.conexao.close()
        except AttributeError:
            pass
    
    def criar_tabelas(self):
        """Cria as tabelas do banco"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    senha VARCHAR(20) NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
                    email TEXT NOT NULL
            );
            """)
        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas')

    def inserir_cliente(self, nome, cpf, email):
        """ INsere cliente no banco"""
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, cpf, email) VALUES(?,?,?)
                """, (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe!' % cpf)
            self.conexao.commit()
        except AttributeError:
            print('Faça conexão com o banco antes de inserir clientes')
    
    def buscar_cliente(self, cpf):
        """ Busca pelo cpf"""
        try:
            cursor = self.conexao.cursor()

            #obtem todos os dados
            #cursor.execute("""SELECT * FROM clientes;""")
            cursor.execute("SELECT * FROM clientes WHERE cpf=?", [(cpf)])

            cliente = cursor.fetchone() # pega o primeiro resultado

            if cliente:
                print('Cliente %s encontrado' % cliente[1])
            else:
                print('Cliente não encontrado')

            #for linha in cursor.fetchall():  caso queira buscar varios
            #  # if linha[2] == cpf:
            # # print('Cliente %s encontrado' % linha[1]) """
        except AttributeError:
            print('Faça a conexão do banco de dados antes de buscar clientes')
        
    def remover_cliente(self, cpf):
        try:
            cursor = self.conexao.cursor()
            cliente = self.buscar_cliente(cpf)
            cursor.execute("""DELETE FROM clientes WHERE cpf== %d""" % int(cpf))
            self.conexao.commit()
            if self.buscar_cliente(cpf) != 'None':
                print(f'O cliente {cliente} foi removido')
            else:
                print("Não temos esse cpf no banco")
        except AttributeError:
            print('Faça a conexão com o banco de dados antes')

    def buscar_email(self, email):
        """Localiza um cliente pelo email"""

        try:
            cursor = self.conexao.cursor()
            cursor.execute("""SELECT * FROM clientes;""")
            for linha in cursor.fetchall():
                if linha[3] == email:	
                    return print(True)
            return False	
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def login(self, username, senha):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM clientes WHERE nome=? and senha=?'
            cliente = cursor.execute(sql, [username, senha]).fetchone()
            if cliente: 
                return True
            else:
                return False
        except AttributeError:
            print("Faça conexão no banco cuzao")