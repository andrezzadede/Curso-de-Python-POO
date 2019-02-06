
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)

    @classmethod
    def de_string(cls, data_string): #10-10-2016
        dia, mes, ano = map(int, data_string.split('-')) #Map pega cada elemento dessa lista e faz uma função, que é a que ta transformando uma string em int
        data = cls(dia, mes, ano) #cls é referencia da classe
        return data
    
    @staticmethod # Ele é uma função dentro de uma classe e ela nao é herdada e nao é possivel subscrever
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2020

data = Data(10, 10, 10)
data1 = data.de_string("10-10-2018")
print(data1)

#O objeto data1 instancia do data e o metodo de classe chama uma nova instancia da classe

vdd = data1.is_date_valid("10-10-2010")
print(vdd)

