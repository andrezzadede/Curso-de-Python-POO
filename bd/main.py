from bdcliente import Cliente

if __name__ == "__main__":
    banco = Cliente()
    banco.conectar()
    banco.criar_tabelas()
    #banco.inserir('Annie', 'Harper', '21321331', 'annied@gmail.com')
    #banco.inserir('Nathan', 'annie', '3923823', 'nathan@gmail.com')
    #banco.inserir('Lauren', 'emm', '3823923', 'laulau@gmail.com')
    #banco.buscar('21321331')
    #banco.buscar('3823923')
    banco.buscar_email('annied@gmail.com')
    #print(banco.login('Annie', 'Harper'))
    #banco.remover('3923823')
    #banco.buscar('3923823')







