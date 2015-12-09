#=========================#
#         tg046           #
#   Andre Fonseca 84698   # 
# Catarina Custodio 84705 #
#=========================#


#==========  TAD coordenada =============#
# a representacao de um coordenada e     #
# um tuplo de 2 elementos, (1) a posicao #
# da linha e (2) a posicao da coluna     #
#========================================#

#_____________Construtor______________
def cria_coordenada(l,c):
    ''' cria_coordenada: int x int -> coordenada
        cria_coordenada (l,c) cria a coordenada de linha l e coluna c'''
    if not(\
            isinstance(l,int) and \
            isinstance(c,int) and \
            l > 0 and c >0):                              # testar se os valores sao inteiros
                raise ValueError('cria_coordenada: argumentos invalidos')
    
    return (l,c)
#fim cria_coordenada




#____________________Selectores______________________
def coordenada_linha(coordenada):
    ''' coordenada_linha: coordenada -> int
        devolve o int da linha correspondente a coordenada'''
    
    return int(coordenada[0])
#fim coordenada_linha
    

def coordenada_coluna(coordenada):
    ''' coordenada_coluna: coordenada - > int
        devolve o int da coluna corresponde a coordenada'''

    return int(coordenada[1])
#fim coordenada_coluna




#__________________Reconhecedores________________________

def e_coordenada(universal):
    ''' e_coordenada: universal -> logico
        devolve True caso o universal seja uma coordenada,
        caso contrario False'''
    if not( isinstance(universal, (tuple)) and\
            len(universal)==2 and\
            isinstance(coordenada_linha(universal),int) and\
            isinstance(coordenada_coluna(universal),int) and\
            coordenada_linha(universal) > 0 and\
            coordenada_coluna(universal) > 0 ):
            return False

    return True
#fim e_coordenada



def coordenadas_iguais(cord1, cord2):
    ''' coordenada_iguais: cordenada x coordenada -> logico
        recebe 2 argumentos (coordenadas) e retorna
        True caso sejam iguais, False caso contrario'''

    return cord1 == cord2 
#fim coordenadas_iguais



#___________________Transformador________________________

def coordenada_para_cadeia(coordenada):
    ''' coordenada_para_cadeia: coordenada -> string
    devolve a representacao da coordenada em string'''

    if not e_coordenada(coordenada):
        raise ValueError('coordenada_para_cadeia: argumentos invalidos')
    
    linha = str(coordenada_linha(coordenada))               # transforma a coordenada da linha numa string
    coluna = str(coordenada_coluna(coordenada))             # transforma a coordenada da coluna numa string
    cadeia = '(' + linha + " : " + coluna + ')'             # junta os varios elementos da string
    
    return cadeia
#fim coordenada_para_cadeia





#==================TAD tabuleiro ==================#
# a repsentacao interna de um tabuleiro e uma      #
# lista com 2 elementos:                           #
# (1) o corpo do tabuleiro que e tambem uma lista  #
# com listas dentro, em que cada lista corresponde #
# a uma linha                                      #
# (2) as especificacoes do tabuleiro               #
#==================================================#

#___________________Construtor_______________________
def cria_tabuleiro(t):
    ''' cria_tabuleiro: tuplo(especificacoes) -> tabuleiro
        devolve um tabuleiro vazio com as dimensoes das especificacoes'''
    if not (e_especificacao(t)):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    tab=[]
    for nr_lin in range (len(t[0])):                  # para cada linha criamos uma lista de zeros
        tab.append([0 for nr_col in range(len(t[1]))]) #com o mesmo numero de colunas

    return [tab,]+[t,]
#fim cria_tabueleiro


# - - Reconhecedor auxliiar ao construtor - - 
def e_especificacao(t):
    ''' e_especificacao: tuplo -> logico
        e_especificacao recebe um tuplo e devolve True caso este
        seja do tipo especificacao, ou caso contrario False'''
    if not (isinstance(t, tuple) and len(t)==2):
        return False 

    for i in range(len(t)):
        if not ( isinstance(t[i],tuple) and len(t[i]) >= 2):
            return False 

        for j in range(len(t[i])):
            if  not isinstance(t[i][j],tuple):
                return False

            for k in range(len(t[i][j])):
                if not((isinstance(t[i][j][k], int)) and t[i][j][k]>=0):
                    return False    
    return True
# fim e_especificacao



#__________________ Selectores ___________________________________

def tabuleiro_dimensoes(tabuleiro):
    '''tabuleiro_dimensoes: tabuleiro -> tuplo
        retorna um tuplo com as dimensoes do tabuleiro'''

    if not(e_tabuleiro(tabuleiro)):                #funcao so valida se recebermos um tabueleiro
        raise ValueError('tabuleiro_dimensoes: argumentos invalidos')
    nr_lin=len(tabuleiro_especificacoes(tabuleiro)[1])
    nr_col=len(tabuleiro_especificacoes(tabuleiro)[0])
    return (nr_lin, nr_col)
# fim tabuleiro_dimensoes # 


def tabuleiro_especificacoes(tabuleiro):
    ''' tabuleiro_especificacoes: tabuleiro -> tuplo
        retorna um tuplo com as especificacoes do tabuleiro'''

    if not(e_tabuleiro(tabuleiro)):
        raise ValueError('tabuleiro_especificacoes: argumentos invalidos')
    
    return tabuleiro[1]
# fim tabuleiro_especificacoes #



def tabuleiro_celula(tabuleiro,coordenada):
    ''' tabuleiro_celula: tabuleiro x coordenada -> int
        devolve o valor da celula correspondente a coordenada no tabuleiro'''

    if not(e_tabuleiro(tabuleiro) \
        and e_coordenada(coordenada)\
        and coordenada_linha(coordenada)<=tabuleiro_dimensoes(tabuleiro)[0]\
        and coordenada_coluna(coordenada)<= tabuleiro_dimensoes(tabuleiro)[0]):
        raise ValueError('tabuleiro_celula: argumentos invalidos') 

    linha = coordenada_linha(coordenada)-1
    coluna = coordenada_coluna(coordenada)-1
    celula = tabuleiro[0][linha][coluna]
    return celula
# fim tabuleiro_celula #



#___________________Transformadores________________________

def tabuleiro_preenche_celula(tabuleiro,coordenada,inteiro):
    ''' tabuleiro_preenche_celula: tabuleiro x coordenada x [0,1,2] -> tabuleiro 
        preenche a celula na coordenada do tabuleiro com o valor inteiro
        e devolve o tabuleiro com a celula preenchida'''

    if not ( e_tabuleiro(tabuleiro)\
            and e_coordenada(coordenada)\
            and isinstance(inteiro,int)\
            and 0<= inteiro<= 2\
            and coordenada_linha(coordenada)<=tabuleiro_dimensoes(tabuleiro)[0]\
            and coordenada_coluna(coordenada)<= tabuleiro_dimensoes(tabuleiro)[0]):
            raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    linha= coordenada_linha(coordenada)
    coluna= coordenada_coluna(coordenada)
    tabuleiro[0][linha-1][coluna-1] = inteiro

    return tabuleiro
# fim tabuleiro_preenche_celula #


def escreve_tabuleiro(tabuleiro):
    ''' escreve_tabuleiro: tabuleiro -> {}
        escreve a estrutura grafica do tabuleiro'''

    if not(e_tabuleiro(tabuleiro)):                #funcao so valida se recebermos um tabueleiro
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    
    especificacoes= tabuleiro_especificacoes(tabuleiro)
    nr_lin_col= tabuleiro_dimensoes(tabuleiro)[0]
    E_lin= especificacoes[0]
    E_col= especificacoes[1]
    dim_Ecol= [len(E_col[x]) for x in range(nr_lin_col)]
    dim_Elin= [len(E_lin[x]) for x in range(nr_lin_col)]
    valores=('?',".","x")
#- - print especificacoes das colunas - -
    for i in range(max(dim_Ecol)):         
        for colunas in range(nr_lin_col):
            if dim_Ecol[colunas]>=max(dim_Ecol)-(i):
                print(' ',E_col[colunas][dim_Ecol[colunas]-max(dim_Ecol)+(i)],end='  ')
            else:
                print('   ',end='  ')   
        print('  ')

#- - print do elemento de cada linha - -
    for l in range (nr_lin_col): 
        for coluna in range(nr_lin_col):
            print ('[',valores[tabuleiro_celula(tabuleiro,cria_coordenada(l+1,coluna+1))],']',end='')

#- - print das especificacoes das colunas - - 
        for i in range(max(dim_Elin)):
            if len(E_lin[l])>=i+1:
                if i==max(dim_Elin)-1:
                    print('',E_lin[l][i],end='')
                else:
                    print('',E_lin[l][i],end='')    
            else:
                if i==max(dim_Elin)-1:
                    print(' ',end=' ')    
                else:
                    print(' ',end=' ')
        print("|")
    print()




#____________________Reconhecedores________________________
def e_tabuleiro(universal):
    ''' e_tabuleiro: universal -> logico
        devolve True se o universal for tabuleiro, caso contrario False'''

    if not( len(universal) == 2\
            and isinstance(universal[0],list)):
            return False

    tab=universal[0]
    especificacoes= universal[1] 
# verifica tab 
    for i in range(len(tab)):      
        if not(len(tab) == len(tab[i])):
            return False

        for j in range(len(tab[i])):
            if not(isinstance(tab,list) \
                    and isinstance(tab[i],list) \
                    and isinstance(tab[i][j],int) \
                    and 0<= tab[i][j] <=2 \
                    ):
                return False
# verificar as especificacoes 
    if not(e_especificacao(especificacoes)):
        return False

    return True 
# fim e_tabuleiro #


def tabuleiros_iguais(tabuleiro_1,tabuleiro_2):
    ''' tabuleiros_iguais: tabuleiro_1 x tabuleiro_2 -> logico
        devolve, True se os 2 tabuleiros forem iguais, caso contrario, False'''

    if not (e_tabuleiro(tabuleiro_1) and e_tabuleiro(tabuleiro_2)):
        return False 
    return tabuleiro_1 == tabuleiro_2
# fim tabuleiros_iguais #



def tabuleiro_completo(tabuleiro):
    ''' tabuleiro_completo: tabuleiro -> logico
        devolve True se o tabuleiro estiver completo seguindo as especificacoes,
        caso contrario devolve False'''

    if not(e_tabuleiro(tabuleiro)):
        return False
    especificacoes=tabuleiro_especificacoes(tabuleiro)
    E_lin=especificacoes[0]
    E_col=especificacoes[1]
    nr_linhas = tabuleiro_dimensoes(tabuleiro)[0]

    if not (tabuleiro_preenchido(tabuleiro)):
        return False 

    for i in range(tabuleiro_dimensoes(tabuleiro)[0]):
        coluna = [tabuleiro_celula(tabuleiro,cria_coordenada((l+1),(i+1))) for l in range (nr_linhas)]
        linha = [tabuleiro_celula(tabuleiro,cria_coordenada((i+1),(c+1))) for c in range (nr_linhas)]
        if not(\
                sum(E_lin[i]) == linha.count(2) and\
                len(E_lin[i])-1 <= linha.count(1) and\
                sum(E_col[i]) == coluna.count(2) and\
                len(E_col[i])-1 <= coluna.count(1)\
                ):
                return False
    return True 
# fim tabuleiro_completo


def tabuleiro_preenchido(tabuleiro):
    ''' tabuleiro -> logico
        retorna True apenas se este nao tiver nenhuma 
        celula a zero, ou seja se estiver preenchido'''

    nr_linhas = tabuleiro_dimensoes(tabuleiro)[0]

    for i in range (nr_linhas):
        for j in range (nr_linhas):
            if tabuleiro_celula(tabuleiro,cria_coordenada(i+1,j+1))==0:
                return False
    return True
# fim tabuleiro_preenchido 





#================= TAD Jogada ========================
# a representacao interna de uma jogada e dada por 
# um tuplo com 2 elementos:
# (1) uma coordenada onde vamos aplicar a jogada
# (2) um valor inteiro (0<valor<=2) que vamos aplicar
#======================================================

#____________________Construtor_________________________

def cria_jogada(coordenada, inteiro):
    ''' cria_jogada: coordenada x inteiro -> jogada
        devolve uma jogada que resulta de juncao de 
        uma coordenada com o valor a ser colocada na celula da coordenada'''

    if not (e_coordenada(coordenada) and isinstance(inteiro,int) and 0<inteiro<=2):
        raise ValueError('cria_jogada: argumentos invalidos')
    jogada = (coordenada,inteiro)
    
    return jogada # para definir jogada temos de definir tabuleiro 
# fim cria_jogada #



#____________________Selectores______________________
def jogada_coordenada(jogada):
    ''' jogada_coordenada: jogada -> tuplo
        devolve o tuplo da coordenada a que corresponde a jogada'''
    
    return jogada[0]
# fim jogada_coordenada #



def jogada_valor(jogada):
    ''' jogada_valor: jogada -> int
        devolve o inteiro correspondente ao valor da jogada'''
    
    return jogada[1]
# fim jogada_valor #



#____________________Reconhecedores________________________

def e_jogada (universal):
    ''' e_jogada: universal -> logico
        devolve se for jogada, True, caso contrario, False'''

    if not( isinstance(universal, tuple)\
            and len (universal)==2\
            and e_coordenada(universal[0])\
            and isinstance(universal[1],int) \
            and 0< universal[1] <= 2):
            return False

    return True 
# fim e_jogada #



def jogadas_iguais (jog1,jog2):
    ''' jogadas_iguais: jogada x jogada -> logico
        devolve True se as 2 jogadas foram iguais, caso contrario False'''

    return jog1 == jog2 
# fim jogadas_iguais #



#_______________________________Transformadores___________________________________

def jogada_para_cadeia(jogada):  #tem de retornar "coordenada --> valor" 
    ''' jogada_para_cadeia: jogada -> string
        devolve a representacao de um jogada em string'''

    coordenada = jogada_coordenada(jogada)
    valor = jogada_valor(jogada)

    return str(str(coordenada_para_cadeia(coordenada))+ " --> " + str(valor))
# fim jogada_para_cadeia #



#_______________________________Funcoes Auxiliares_________________________________
def le_tabuleiro(string):
    ''' le_tabuleiro: string -> tuplo
        devolve o tuplo lido do ficheiro do nome string'''

    ficheiro=open(string,"r")
    especificacoes = eval (ficheiro.readline())
    ficheiro.close()

    return especificacoes
# fim le_tabuleiro #




def pede_jogada(tabuleiro):
    ''' pede_jogada: tabuleiro -> jogada
        devolva a jogada que o jogador quer executar'''
#recebe os inputs da jogada 
    if not e_tabuleiro(tabuleiro):
        raise ValueError('e_tabuleiro: argumentos invalidos')
    string = input ('Introduza a jogada\n- coordenada entre (1 : 1) e '+\
                coordenada_para_cadeia(tabuleiro_dimensoes(tabuleiro))+' >> ')
    valor = input ("- valor >> ")

# avalia o input 

    string = string.replace(' ','').replace('(','').replace(')','')
    coords = string.split(':')
    
# verifica a avaliacao do input 
    if valor.isdigit():
        valor = int(valor)
    if not( len(coords)==2\
            and coords[0].isdigit\
            and coords[1].isdigit):
        return False 
    
    coord0 = int(coords[0])
    coord1 = int(coords[1])
    nr_linhas = tabuleiro_dimensoes(tabuleiro)[0]

    if not (coord0 <= nr_linhas and coord1 <= nr_linhas):
        return False
    return cria_jogada(cria_coordenada(coord0,coord1),valor)

# fim pede_jogada #






#______________________________ Funcao Principal ______________________
def jogo_picross (string):
    ''' jogo_picross: string-> logico
        funcao que permite jogar o jogo, pedindo jogadas e aplicando ao tabuleiro
        retorna: True se o Jogo estiver completo (bem preenchido)
        retorna: False se o jogo estiver mal completo (mal preenchido)'''
    
    print('JOGO PICROSS')
    especificacoes = le_tabuleiro(string)
    tabuleiro = cria_tabuleiro(especificacoes)
    escreve_tabuleiro(tabuleiro)
    #jogada_anterior = 0 
    
# enquanto o tabuleiro nao estiver completo jogamos
    while not (tabuleiro_completo(tabuleiro)):
        if (tabuleiro_preenchido(tabuleiro)):
            print('JOGO: O tabuleiro nao esta correto!')
            return False

        jogada = pede_jogada(tabuleiro)
            
        if not e_jogada(jogada):
            print('Jogada invalida.')

# aplicar mudanca caso possivel                 
        if e_jogada(jogada):
            #jogada_anterior=jogada 
            tabuleiro_preenche_celula(tabuleiro, jogada_coordenada(jogada),jogada_valor(jogada))
            escreve_tabuleiro(tabuleiro)

    print ('JOGO: Parabens, encontrou a solucao!')
    return True 
#fim jogo_picross<

