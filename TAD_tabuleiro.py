
#def cria_tabuleiro(t):
#	if isinstance(t[0],(tuple)) and isinstance(t[1], (tuple)):
#		for i in (0, len(t[0])-1):
#			if isinstance(t[0][i], (tuple)) and isinstance(t[1][i], (tuple)):
#				tabuleiro = t
#				return tabuleiro
#			else:
#				raise ValueError('cria_tabuleiro: argumentos invalidos')
#	else:
#		raise ValueError('cria_tabuleiro: argumentos invalidos')
	


def tabuleiro_dimensoes(t):
	nr_linhas = len(t[0])
	nr_colunas = len(t[1])
	return (nr_linhas, nr_colunas)


#def tabuleiro_especificacoes(t):
#	return cria_tabuleiro(t)

