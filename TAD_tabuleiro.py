
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

#TAD tabuleiro
def cria_tabuleiro(tuplo):
    tabuleiro_pt1=[]
    for nr_de_linhas in range (len(tuplo[0])):                  # para cada linha criamos uma lista de zeros
        tabuleiro_pt1.append([0 for nr_colunas in range(len(tuplo[1]))]) #com o mesmo numero de colunas 
    especificacoes=[tuplo,]                                              # que as especificacoes
    return [tabuleiro_pt1,]+especificacoes
# representacao interna: e uma lista em que o primeiro elemento e a parte do tabuleiro onde entram
# as jogadas e o segundo elemento e o tuplo das especificacoes   

def tabuleiro_dimensoes(tabuleiro):
    '''recebe um elemento do tipo tabuleiro e retorna um tuplo
     com as dimensoes deste (linhas,colunas)'''
    numero_linhas=len(tabuleiro[0])
    numero_colunas=len(tabuleiro[0][0])
    if not(e_tabuleiro(tabuleiro)):                #funcao so valida se recebermos um tabueleiro
        raise ValueError('tabuleiro_dimensoes: argumentos invalidos')
    return (numero_linhas, numero_colunas)

def tabuleiro_especificacoes(tabuleiro):
    ''' recebe um tabuleiro e retornar as especificacoes deste'''
    if not(e_tabuleiro(tabuleiro)):
        raise ValueError('tabuleiro_especificacoes: argumentos invalidos')
    return tabuleiro[1]

def tabuleiro_celula(tabuleiro,coordenada):
    ''' recebe um tabuleiro e uma coordenada, retorna um elemento do tipo inteiro entre 0 e 2
    que corresponde ao valor contido na celula da coordenada: 0 se vazia, 1 se estiver branco
    e 2 se estiver preenchido'''
    #if not(e_tabuleiro(tabuleiro) and e_coordenada(coordenada)):
        #raise ValueError('tabuleiro_celula: argumentos invalidos')
        #nao definida a e_coordenada no meu programa ainda 
    return tabuleiro[coordenada[0]-1][coordenada[1]-1] # primeiro ve a linha e depois coluna


def tabuleiro_preenche_celula(tabuleiro,coordenada,inteiro):
    '''recebe um tabuleiro, uma coordenada e um inteiro entre 0 2, modifica o tabuleiro
    e preenche a celula da coordenada com o inteiro, retornando o tabuleiro modificado'''
    # ValueError com a mensagem ’tabuleiro_preenche_celula: argumentos invalidos’ caso algum
    # dos argumentos introduzidos não seja válido.
    
    #if not(e_tabuleiro(tabuleiro) and e_coordenada(coordenada) and isinstance(inteiro,int)):
        #raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
        #nao definida a e_coordenada no meu programa ainda 
    tabuleiro[coordenada[0]-1][coordenada[1]-1]=inteiro
    return tabuleiro # nao testada mas em principio deve funcionar


def e_tabuleiro(universal):
    '''verificar se um universal e um tabuleiro ou nao, retornando true ou false'''
    try:
        tabuleiro=universal[0]
        especificacoes= universal[1]
        nr_linhas= len(tabuleiro)

        if not (len(universal)==2 and\
            isinstance(tabuleiro,list) and\
            isinstance(especificacoes, tuple)): # o tabuleiro e uma lista com listas
            return False                        # as especificacoes e um tuplo

            #verificar tabuleiro
        for i in range(len(tabuleiro)):      
            nr_colunas = len(tabuleiro[i]) #o nr de linhas tem de ser = ao nr colunas
            if not(nr_colunas == nr_linhas and isinstance(tabuleiro[i], list)):
                return False

            for j in range(len(tabuleiro[i])):
                elemento=tabuleiro[i][j]
                if not ((isinstance(elemento,int) and 0<=elemento<=2)): #todos elementos do tabuleiro
                    return False                                        #sao inteiros >=0 e <=2
        
            # verificar especificacoes
        if not(e_especificacao(especificacoes)):
        	return False

    except(RuntimeError, TypeError, NameError): # caso alguma das operacoes acima nao seja possivel
        return False                            # entao nao e um tabuleiro
    return True 

# teste: print(e_tabuleiro(cria_tabuleiro((((2, ), (3, ), (2, ), (2, 2), (2, )), ((2, ), (1, 2), (2, ), (3, ), (3, ))))))


def tabuleiros_iguais(tabuleiro_1,tabuleiro_2):
    if not (e_tabuleiro(tabuleiro_1) and e_tabuleiro(tabuleiro_2)):
        raise ValueError('cria_jogada: argumentos invalidos')
    
    tab1=tabuleiro_1[0]
    espec_1=tabuleiro_especificacoes(tabuleiro_1)
    tab2=tabuleiro_2[0]
    espec_2=tabuleiro_especificacoes(tabuleiro_2)

    if not(tab1==tab2 and espec_1==espect_2):
        return False
    return True


def escreve_tabuleiro(tabuleiro):

    if not(e_tabuleiro(tabuleiro)):                #funcao so valida se recebermos um tabueleiro
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    
    tab=tabuleiro[0]
    especificacoes= tabuleiro_especificacoes(tabuleiro)
    E_lin= especificacoes[0] #especificacoes das colunas
    E_col = especificacoes[1] #especificacoes das linhas
    nr_lin_col=len(tab) #numero de linhas e colunas
    dim_Ecol=[len(E_col[x]) for x in range(nr_lin_col)] #len dos numeros
    num_max_Ecol= max(dim_Ecol)
    dim_Elin=[len(E_lin[x]) for x in range(nr_lin_col)]
    num_max_Elin= max(dim_Elin)
    valores=('?',".","x")


    for nr_espec in range(num_max_Ecol):          # print especificacoes das colunas
        for colunas in range(nr_lin_col):
            if dim_Ecol[colunas]-1>=(num_max_Ecol-1)-(nr_espec):
                print(' ',E_col[colunas][dim_Ecol[colunas]-num_max_Ecol+(nr_espec)],end='   ')
            else:
                print('   ',end='   ')
                
        print()

    for linha in range (nr_lin_col): # print de cada elemento 
        for coluna in range(nr_lin_col):
            valor = tab[linha][coluna]
            print ('[',valores[valor],']',end=' ')
        for nr_espec in range(num_max_Elin):
            try: 
                if nr_espec==num_max_Elin-1:
                    print(E_lin[linha][nr_espec],end='')    
                else:
                    print(E_lin[linha][nr_espec],end=' ')
            except(IndexError):
                if nr_espec==num_max_Elin-1:
                    print('',end=' ')    
                else:
                    print(' ',end=' ')
        print("|")
        
# para testar:  cria_tabuleiro((((2, ), (3, ), (2, ), (2, 2), (2, )), ((2, ), (1, 2), (2, ), (3, ), (3, ))))
# retorna :[[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], (((2,), (3,), (2,), (2, 2), (2,)), ((2,), (1, 2), (2,), (3,), (3,)))]
#--------------------------------------------



def e_especificacao(t):
	for i in range(len(t)):
		for j in range(len(t[i])):
			for k in range(len(t[i][j])):
				if not(isinstance(t, tuple)) or\
				   not(isinstance(t[i], tuple)) or\
				   not(isinstance(t[i][j], tuple)) or\
				   not((isinstance(t[i][j][k], int)) and t[i][j][k]>0):
					return False
	return True


def tabuleiro_completo(t):
	

def tabuleiros_iguais(t1, t2):
	

def escreve_tabuleiro(t):
	
#pepe sucks 
