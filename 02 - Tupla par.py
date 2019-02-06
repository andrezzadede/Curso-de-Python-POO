# Tupla Par
# Vamos resolver um exercicio que envolve tuplas? Você deverá  desenvolver uma função chamada tupla_par. Essa função recebe uma tupla como entrada e retorna uma nova tupla como saída onde os elementos dessa nova tupla são os elementos cujos índices são números pares. Lembrando que o Python indexa a partir do zero.
# Exemplo de tupla de entrada: ('oi', 'estou', 'estudando', 'poo')
# Tupla que deve ser retornada: ('oi', 'estudando')

def tupla_par(tupla):
	lista = list()
	i = 0
	while i < len(tupla):
		if i % 2 == 0:
			lista.append(tupla[i])
		i += 1
	tupla2 = tuple(lista)
	return tupla2
	
	
tupla = (0, 1, 2, 3, 4, 5, 6, 7)
print(tupla_par(tupla))
