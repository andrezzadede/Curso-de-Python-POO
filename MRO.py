# MRO - Method Resolution order

# Em heranças, ele mosstra a ordem que cada uma é chamada

class Veiculo():
    def __init__(self):
        pass
     

class Carro(Veiculo):
    def __init__(self):
        super(Carro, self).__init__()

class Trem(Veiculo):
    pass

class CarroTrem(Carro, Trem):
    pass


print(Veiculo.__mro__)
print(Carro.__mro__)
print(CarroTrem.__mro__)