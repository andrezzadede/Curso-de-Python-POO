'''
Quando utilizar?

Se você desejar reutilizar uma determinada feature(caracteristica) em várias classes diferentes. 
Para melhorar a modularidade

Mixins é uma forma controlada de adicionar funcionalidades as classes

Propriedades: 

Nao deve ser extendida
Não deve ser instanciada

Em Python, o conceito de mixins é implementado utilizando herança multipla

'''

class Livro(object):
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo


class LivroHTMLMixin(object):
    def renderizar(self):
        return ('<html><title>%s</title><body>%s</body></html>') % (self.nome, self.conteudo)


class LivroHTML(Livro, LivroHTMLMixin):
    pass


livro_html = LivroHTML('Toda Sua', 'Eva e Gideon')
print(livro_html.renderizar())