
def cria_tabuleiro(t):
	if isinstance(t[0],(tuple)) and isinstance(t[1], (tuple)):
		for i in (0, len(t[0])-1):                                             # uma vez que o tabuleiro e nxn, nr_linhas = nr_colunas
			if isinstance(t[0][i], (tuple)) and isinstance(t[1][i], (tuple)):  # falta definir que dentro dos tuplos sejam num_inteiros
				tabuleiro = t
				return tabuleiro
			else:
				raise ValueError('cria_tabuleiro: argumentos invalidos')
	else:
		raise ValueError('cria_tabuleiro: argumentos invalidos')
	

def tabuleiro_dimensoes(t):
	nr_linhas = len(t[0])
	nr_colunas = len(t[1])
	return (nr_linhas, nr_colunas)


def tabuleiro_especificacoes(t):
	return cria_tabuleiro(t)


def tabuleiro_celula(t, c):
	

def tabuleiro_preenche_celula(t, c, e):                                      # t = tabuleiro, c = coordenada e e = inteiro {0, 1, 2}
	

def e_tabuleiro(t):


def tabuleiro_completo(t):
	

def tabuleiros_iguais(t1, t2):
	

def escreve_tabuleiro(t):
	