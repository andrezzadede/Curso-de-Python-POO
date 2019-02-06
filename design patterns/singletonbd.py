# Exemplo práatico Singleton - Banco de Daados

#Sqlite biblioteca para bd (Se for usar para caralho,não é recomendavel)

import sqlite3

class MetaSingleton(type): #Metaclasse sempre vai herdar de type
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('banco.db')
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = Database().connect()
db2 = Database().connect()

print(db1, db2)

#Ela será instanciada varias vezes, mas apenas um objeto será criado. Ou seja as chamadas do banco serao sincronizadas. 
