#=========================#
#         tg046           #
#   Andre Fonseca 84698   # 
# Catarina Custodio 84705 #
#=========================#


###############################################################################################################################
#                                               TAD_coordenadas                                                               #
###############################################################################################################################

def cria_coordenada(l, c):
	if not(verifica_coordenada(l,c)):                                               # utiliza uma funcao auxiliar para verificar as condicoes
		raise ValueError('cria_coordenada: argumentos invalidos')
	else:
		return (l,c)

############## Funcao Auxiliar ###################

def verifica_coordenada(l,c):
	if not(isinstance(l,(int)) and isinstance(c,(int))):			        # testar se os valores sao inteiros
		return False
	if l <= 0 or c <= 0:							        # testar se os valores sao positivos
		return False
	else:
		return True

##################################################
	
	
def coordenada_linha(coordenada):						        # o primeiro valor do tuplo da a coordenada da linha
	return coordenada[0]
	
	
def coordenada_coluna(coordenada):
	return coordenada[1]					                        # o segundo valor do tuplo da a coordenada da coluna 

	
def e_coordenada(coordenada):					                # testar se os dados inseridos correspondem ao tipo coordenada	
	if isinstance(coordenada, tuple):
		return verifica_coordenada(coordenada_linha(coordenada), coordenada_coluna(coordenada))
	else:
		return False                                    	                # caso nao seja tuplo, retorna False


def coordenadas_iguais(coordenada1, coordenada2):
	if coordenada_linha(coordenada1) == coordenada_linha(coordenada2) and coordenada_coluna(coordenada1) == coordenada_coluna(cordenada2):	        		
		return True
	else:									        
		return False


def coordenada_para_cadeia(coordenada):
	linha = str(coordenada_linha(coordenada))			                # transforma a coordenada da linha numa string
	coluna = str(coordenada_coluna(coordenada))			                # transforma a coordenada da coluna numa string
	cadeia = '(' + linha + " : " + coluna + ')'			                # junta os varios elementos da string
	return cadeia


	
#################################################################################################################################
#                                             TAD_Tabuleiro                                                                     #
#################################################################################################################################

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


def cria_tabuleiro(t):							# nao terminada!!!
	if e_tabuleiro(t):
		return t
	else:
		raise ValueError('cria_tabuleiro: argumentos invalidos')
	