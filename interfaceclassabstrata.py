# Classe abstrata ou interface
#Uma classe abstrata nãoo pode ser diretamente instanciada, ela serve apenas para que outras classes possam ter ela como base

from abc import ABCMeta, abstractmethod

class MinhaClasseAbstrata(metaclass=ABCMeta):
    
    @abstractmethod
    def fazer_algo(self):
        pass

    @abstractmethod
    def fazer_algo_novamente(self, o_que_fazer):
        pass
    


    