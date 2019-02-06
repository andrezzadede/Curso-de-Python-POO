""" Criação de tabelas"""

from bdconexao import Database
import sqlite3

class Cliente(Database):    
    def criar_tabelas(self):
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
            print('Faça conexão com o banco antes da criação de tabelas')

    def inserir(self, nome, senha, cpf, email):
        try: 
            cursor = self.conexao.cursor()

            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)
                """, (nome, senha, cpf, email))
            except sqlite3.IntegrityError:
                print('O CPF %s já existe!' % cpf)
            
            self.conexao.commit()

        except AttributeError:
            print('Faça a conexão com o banco antes de inserir o cliente')
    
    def buscar(self, cpf):
        try:
            cursor = self.conexao.cursor()

            cursor.execute("SELECT * FROM clientes WHERE cpf=?", [(cpf)])
            cliente = cursor.fetchone()

            if cliente:
                print(f'Cliente {cliente[1]} encontrado')
            else:
                print(f'Cliente {cpf} não encontrado')
        except AttributeError:
            print('Faça a conexão com o banco antes da busca')
    
    def remover(self, cpf):
        try:
            cursor = self.conexao.cursor()
            cliente = self.buscar(cpf)
            cursor.execute(""" DELETE FROM clientes WHERE cpf == %d""" % int(cpf))
            self.conexao.commit()
            if self.buscar(cpf) != 'None':
                print(f'O cliente {cliente} foi removido')
            else:
                print(f'Não temos informações sobre esse número de {cpf} cpf')
        except AttributeError:
            print('Faça a conexão com o banco de dados antes')
    
    def buscar_email(self, email):
        """Localiza um cliente pelo email"""

        try:
            cursor = self.conexao.cursor()
            
            cursor.execute("SELECT * FROM clientes where email=?", [(email)])
            cliente = cursor.fetchone()
            
            if cliente:
                print(f'Cliente {cliente[1]} encontrado')
            else:
                print(f'Cliente {email} não encontrado')
        except AttributeError:
            print('Faça a conexão com o banco antes')
    
    def login(self, username, senha):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM clientes WHERE nome=? and senha =?'
            cliente = cursor.execute(sql, [username, senha]).fetchone()
            if cliente:
                return True
            else:
                return True
        except AttributeError:
            print('Faça a conexão com o banco antes')


