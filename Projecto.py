#=========================#
#         tg046           #
#   Andre Fonseca 84698   # 
# Catarina Custodio 84705 #
#=========================#


########################TAD_coordenadas#########################################################################################

def cria_coordenada(l, c):
	if not(isinstance(l,(int)) and isinstance(c,(int))):			# testar se os valores sao inteiros
		raise ValueError('cria_coordenada: argumentos invalidos')
	if l <= 0 or c <= 0:							# testar se os valores sao positivos
		raise ValueError('cria_coordenada: argumentos invalidos')
	else:
		return (l,c)

	
def coordenada_linha(coordenada):						# o primeiro valor do tuplo da a coordenada da linha
	return coordenada[0]
	
	
def coordenada_coluna(coordenada):
	return coordenada[1]					# o segundo valor do tuplo da a coordenada da coluna 

	
def e_coordenada(coordenada):
	if isinstance(coordenada, (tuple)):							# verificar se o que e dado e um tuplo
		if not(isinstance(coordenada_linha(coordenada),(int)) and \
		isinstance(coordenada_coluna(coordenada),(int))):	# verificar que os elementos do tuplo sao inteiros
			return False
		if coordenada_linha(coordenada) <= 0 or coordenada_coluna(coordenada) <= 0:	# verificar que os elementos do tuplo sao positivos
			return False
		else:										# caso contrario, e coordenada
			return True
	else:
		return False									# caso nao seja tuplo, retorna False


def coordenadas_iguais(coordenada1, coordenada2):
	if coordenada_linha(coordenada1) == coordenada_linha(coordenada2) and \
	coordenada_coluna(coordenada1) == coordenada_coluna(cordenada2):	#comparar posicao 1 das coordenadas, e fazer o mesmo para a posicao 2		
		return True
	else:									# caso sejam diferentes, retorna False
		return False


def coordenada_para_cadeia(coordenada):
	linha = str(coordenada_linha(coordenada))			# transforma a coordenada da linha numa string
	coluna = str(coordenada_coluna(coordenada))			# transforma a coordenada da coluna numa string
	cadeia = '(' + linha + " : " + coluna + ')'			# junta os varios elementos da string
	
	return cadeia
	
#################################################################################################################################
