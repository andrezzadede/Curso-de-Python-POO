def funcao(*args): #Args é usado por convenção, mas pode ser qualquer nome
    print(args)

funcao(1,2,4, 'Annie')

#Caso eu queira fazer em estilo lista

def funk(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

funk(nome= 'Annie', idade= 23, linguagem= 'python' )