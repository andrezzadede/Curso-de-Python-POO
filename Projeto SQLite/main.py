from database import BancoDeDados

if __name__ == "__main__":
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()
    banco.inserir_cliente('Annie', 'harper' '23223143', 'annied@gmail.com')
    banco.inserir_cliente('Nathan', 'delacroix' '88299492', 'nathanharper@gmail.com')

    # banco.remover_cliente('88299492')

    #banco.buscar_email('annied@gmail.com')

    
    #banco.buscar_cliente('88299492')
    print(banco.login('Annie', 'harper'))
    
    banco.desconectar()


