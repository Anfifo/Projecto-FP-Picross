
def cria_tabuleiro(t):
	if isinstance(t[0],(tuple)) and isinstance(t[1], (tuple)):
		for i in (0, len(t[0])-1):                                             	   # uma vez que o tabuleiro e nxn, nr_linhas = nr_colunas
			if isinstance(t[0][i], (tuple)) and isinstance(t[1][i], (tuple)):  # falta definir que dentro dos tuplos sejam num_inteiros
				tabuleiro = t
				return tabuleiro
			else:
				raise ValueError('cria_tabuleiro: argumentos invalidos')
	else:
		raise ValueError('cria_tabuleiro: argumentos invalidos')
	
# catarina,  essa que esta ai em cima é aquela antiga tua que tinha um erro neh? olha ve como achas da maneira
# como esta definido aqui em baixo

# eu depois tinha atualizado a e_tabuleiro no Projecto.py

def cria_tabuleiro(tuplo):
    tabuleiro_pt1=[]
    for nr_de_linhas in range (len(tuplo[0])):
        tabuleiro_pt1.append([0 for nr_colunas in range(len(tuplo[1]))])
    especificacoes=[tuplo,]
    return [tabuleiro_pt1,]+especificacoes
# retorna um tabuleiro vazio no primeiro elemento e as especificacoes no segundo elemento 
# e ATENCÃO: A FUNÇÃO TEM DE TESTAR AS CONDIÇÕES!!, por isso vamos ter de utilizar outro sistema em vez do das posições...

#(Andre): afinal nao achei tao boa ideia juntar tudo numa so por isso pus assim, estamos com as cenas separadas 



# para testar:  cria_tabuleiro((((2, ), (3, ), (2, ), (2, 2), (2, )), ((2, ), (1, 2), (2, ), (3, ), (3, ))))
# retorna :[[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], (((2,), (3,), (2,), (2, 2), (2,)), ((2,), (1, 2), (2,), (3,), (3,)))]
#--------------------------------------------


def tabuleiro_dimensoes(t):
	nr_linhas = len(t[0])
	nr_colunas = len(t[1])
	return (nr_linhas, nr_colunas)


def tabuleiro_especificacoes(t):
	return cria_tabuleiro(t)


def tabuleiro_celula(t, c):
	

def tabuleiro_preenche_celula(t, c, e):                                      # t = tabuleiro, c = coordenada e e = inteiro {0, 1, 2}
	

def e_tabuleiro(t):
	for i in range(len(t)):
		for j in range(len(t[i])):
			for k in range(len(t[i][j])):
				if not(isinstance(t, tuple)) or\
				   not(isinstance(t[i], tuple)) or\
				   not(isinstance(t[i][j], tuple)) or\
				   not(isinstance(t[i][j][k], int)):
					return False
	return True


def tabuleiro_completo(t):
	

def tabuleiros_iguais(t1, t2):
	

def escreve_tabuleiro(t):
	
#pepe sucks 
