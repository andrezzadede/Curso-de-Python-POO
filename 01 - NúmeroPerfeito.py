# Um número perfeito é um numero inteiro cujo a soma de todos os seus divisores positivos (excluindoo proprio numero) é igual a ele
# Exemplo 28 é um numero perfeito, pois seus divisores: 1,2,4,7,14 = 28
#Desenvolva a função numero perfeito que recebera como entrada um número e retornara True se ele for perfeito e false caso contrário

n = int(input('Fale o numero'))

def numero_perfeito(num):
	cont = 1
	soma = 0
	while cont<num:
		if num % cont == 0:
			soma = soma + cont
		cont = cont + 1
	if soma == num:
		return True
		print('true')
	else:
		return False
		print('false')

numero_perfeito(n)
