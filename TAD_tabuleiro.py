
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

def cria_tabuleiro(tuplo):
    #len do primeiro tuplo = numero de colunas
    #len do segundo tuplo= numero de linhas 
    #numero de linhas = numero de colunas 
    tabuleiro_pt1=[]
    for nr_de_linhas in range (len(tuplo[0])):
        tabuleiro_pt1.append(tuple([0 for nr_colunas in range(len(tuplo[1]))])+(tuplo[1][nr_de_linhas],))  #juntar a base 
                                                                #do tabueliro as especificacoes (possivelmente fazer uma funcao?)
    tabuleiro = list(tuple(tuplo[0])+tuple(tabuleiro_pt1))
    return tabuleiro 

# para testar:  cria_tabuleiro((((2, ), (3, ), (2, ), (2, 2), (2, )), ((2, ), (1, 2), (2, ), (3, ), (3, ))))
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


def tabuleiro_completo(t):
	

def tabuleiros_iguais(t1, t2):
	

def escreve_tabuleiro(t):
	
