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
    
    if not e_coordenada(coordenada):
        raise ValueError("coordenada_linha: argumentos invalidos")
    
    return int(coordenada[0])
#fim coordenada_linha
    

def coordenada_coluna(coordenada):
    ''' coordenada_coluna: coordenada - > int
        devolve o int da coluna corresponde a coordenada'''
    
    if not e_coordenada(coordenada):
        raise ValueError("coordenada_coluna: argumentos invalidos")
    return int(coordenada[1])
#fim coordenada_coluna




#__________________Reconhecedores________________________

def e_coordenada(universal):
    ''' e_coordenada: universal -> logico
        devolve True caso o universal seja uma coordenada,
        caso contrario False'''
    
    try:
        if not(\
                isinstance(universal, (tuple)) and\
                isinstance(universal[0],int) and\
                isinstance(universal[1],int) and\
                universal[0] > 0 and\
                universal[1] > 0\
                ):
                return False
    except(IndexError,TypeError,NameError):
        return False

    return True
#fim e_coordenada



def coordenadas_iguais(cord1, cord2):
    ''' coordenada_iguais: cordenada x coordenada -> logico
        recebe 2 argumentos (coordenadas) e retorna
        True caso sejam iguais, False caso contrario'''

    if not (e_coordenada(cord1) and e_coordenada(cord2)):
        raise ValueError('coordenadas_iguais: argumentos invalidos') 
    if not (\
            coordenada_linha(cord1) == coordenada_linha(cord2) and\
            coordenada_coluna(cord1) == coordenada_coluna(cord2)\
            ):       # comparar a posicao 1 das duas coordenadas, e fazer o mesmo para a segunda coordenada
            return False
    
    return True 
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
def cria_tabuleiro(tuplo):
    ''' cria_tabuleiro: tuplo(especificacoes) -> tabuleiro
        devolve um tabuleiro vazio com as dimensoes das especificacoes'''

    if not (e_especificacao(tuplo)):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    tab=[]
    for nr_lin in range (len(tuplo[0])):                  # para cada linha criamos uma lista de zeros
        tab.append([0 for nr_col in range(len(tuplo[1]))]) #com o mesmo numero de colunas

    return [tab,]+[tuplo,]
#fim cria_tabueleiro


# - - Reconhecedor auxliiar ao construtor - - 
def e_especificacao(t):
    ''' e_especificacao: tuplo -> logico
        e_especificacao recebe um tuplo e devolve True caso este
        seja do tipo especificacao, ou caso contrario False'''
    
    try:
        for i in range(len(t)):
            for j in range(len(t[i])):
                for k in range(len(t[i][j])):
                    if not(isinstance(t, tuple)) or\
                        not(isinstance(t[i], tuple)) or\
                        not(isinstance(t[i][j], tuple)) or\
                        not((isinstance(t[i][j][k], int)) and t[i][j][k]>=0):
                        return False
    except(TypeError,IndexError):
        return False 
    
    return True
# fim e_especificacao



#__________________ Selectores ___________________________________

def tabuleiro_dimensoes(tabuleiro):
    '''recebe um elemento do tipo tabuleiro e retorna um tuplo
     com as dimensoes deste (linhas,colunas)'''
    
    if not(e_tabuleiro(tabuleiro)):                #funcao so valida se recebermos um tabueleiro
        raise ValueError('tabuleiro_dimensoes: argumentos invalidos')
    nr_lin=len (tabuleiro_especificacoes(tabuleiro)[1])
    nr_col=len(tabuleiro_especificacoes(tabuleiro)[0])
    return (nr_lin, nr_col)
# fim tabuleiro_dimensoes # 


def numero_linhas (tabuleiro):
    return coordenada_linha(tabuleiro_dimensoes(tabuleiro))
# fim numero_linhas #


def numero_colunas (tabuleiro):
    return coordenada_coluna(tabuleiro_dimensoes(tabuleiro))
# fim numero_colunas #


def tabuleiro_especificacoes(tabuleiro):
    ''' recebe um tabuleiro e retornar as especificacoes deste'''
    if not(e_tabuleiro(tabuleiro)):
        raise ValueError('tabuleiro_especificacoes: argumentos invalidos')
    return tabuleiro[1]
# fim tabuleiro_especificacoes #


def tabuleiro_celula(tabuleiro,coordenada):
    ''' recebe um tabuleiro e uma coordenada, retorna um elemento do tipo inteiro entre 0 e 2
    que corresponde ao valor contido na celula da coordenada: 0 se vazia, 1 se estiver branco
    e 2 se estiver preenchido'''
    if not(e_tabuleiro(tabuleiro) and e_coordenada(coordenada)):
        raise ValueError('tabuleiro_celula: argumentos invalidos') 
    try:    
        linha = coordenada_linha(coordenada)-1
        coluna = coordenada_coluna(coordenada)-1
        celula = tabuleiro[0][linha][coluna]
    except(TypeError,NameError,ValueError,IndexError):
        raise ValueError('tabuleiro_celula: argumentos invalidos')   
    return celula
# fim tabuleiro_celula #


#___________________Transformadores________________________

def tabuleiro_preenche_celula(tabuleiro,coordenada,inteiro):
    '''recebe um tabuleiro, uma coordenada e um inteiro entre 0 2, modifica o tabuleiro
    e preenche a celula da coordenada com o inteiro, retornando o tabuleiro modificado'''   
    if not (e_tabuleiro(tabuleiro) and e_coordenada(coordenada) and\
            isinstance(inteiro,int) and 0<= inteiro<= 2 ):
            raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    try:
        linha= coordenada_linha(coordenada)
        coluna= coordenada_coluna(coordenada)
        tabuleiro[0][linha-1][coluna-1] = inteiro

    except(TypeError,NameError,ValueError,IndexError):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    return tabuleiro
# fim tabuleiro_preenche_celula #


def escreve_tabuleiro(tabuleiro):
    if not(e_tabuleiro(tabuleiro)):                #funcao so valida se recebermos um tabueleiro
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    
    especificacoes= tabuleiro_especificacoes(tabuleiro)
    nr_lin_col= numero_colunas(tabuleiro)
    E_lin= especificacoes[0] 
    E_col= especificacoes[1]  
    dim_Ecol= [len(E_col[x]) for x in range(nr_lin_col)]
    dim_Elin= [len(E_lin[x]) for x in range(nr_lin_col)]
    valores=('?',".","x")
    tab=tabuleiro[0]

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
            print ('[',valores[tab[l][coluna]],']',end='')

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
    '''verificar se um universal e um tabuleiro ou nao, retornando true ou false'''
    try:
        tab=universal[0]
        especificacoes= universal[1]
        nr_linhas= len(tab) 
# verifica tab 
        for i in range(len(tab)):      
            nr_colunas = len(tab[i]) #o nr de linhas tem de ser = ao nr colunas
            for j in range(len(tab[i])):
                if not(\
                    0<= tab[i][j] <=2 and\
                    len(universal) == 2 and\
                    isinstance(tab,list) and\
                    nr_colunas==nr_linhas and\
                    isinstance(tab[i],list) and\
                    isinstance(tab[i][j],int) and\
                    isinstance(especificacoes,tuple)\
                    ):
                    return False
# verificar as especificacoes 
        if not(e_especificacao(especificacoes)):
            return False
    except(RuntimeError, TypeError, NameError,IndexError): # caso alguma das operacoes acima nao seja possivel
        return False                            # entao nao e um tabuleiro
    return True 
# fim e_tabuleiro #


def tabuleiros_iguais(tabuleiro_1,tabuleiro_2):
    if not (e_tabuleiro(tabuleiro_1) and e_tabuleiro(tabuleiro_2)):
        raise ValueError('cria_jogada: argumentos invalidos')
    try:
        tab1=tabuleiro_1[0]
        tab2=tabuleiro_2[0]
        espec_1=tabuleiro_especificacoes(tabuleiro_1)
        espec_2=tabuleiro_especificacoes(tabuleiro_2)

        for lin in range(len(tab1)):
            for col in range (len(tab1[lin])):
                if not(\
                    tab1[lin][col]==tab2[lin][col] and\
                    espec_1[0][lin]==espec_2[0][lin]and\
                    espec_1[1][col]==espec_2[1][col]\
                    ):
                    return False
    except(IndexError,TypeError):
        return False  
    return True
# fim tabuleiros_iguais #



def tabuleiro_completo(tabuleiro):
    if not(e_tabuleiro(tabuleiro)):
        raise ValueError('tabuleiro_completo: argumentos invalidos')
    especificacoes=tabuleiro_especificacoes(tabuleiro)
    E_lin=especificacoes[0]
    E_col=especificacoes[1]

    if not (tabuleiro_preenchido(tabuleiro)):
        return False 

    for i in range (coordenada_linha(tabuleiro_dimensoes(tabuleiro))):
        coluna = [tabuleiro_celula(tabuleiro,cria_coordenada((l+1),(i+1))) for l in range (coordenada_linha(tabuleiro_dimensoes(tabuleiro)))]
        linha = [tabuleiro_celula(tabuleiro,cria_coordenada((i+1),(c+1))) for c in range (coordenada_linha(tabuleiro_dimensoes(tabuleiro)))]
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
    ''' tabuleiro -> boleano
        recebe um tabuleiro e retorna True apenas se este nao tiver 
        nenhuma celula a zero, ou seja se estiver preenchido'''
    for i in range (coordenada_linha(tabuleiro_dimensoes(tabuleiro))):
        for j in range (coordenada_coluna(tabuleiro_dimensoes(tabuleiro))):
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
    if not (e_coordenada(coordenada) and 0<inteiro<=2):
        raise ValueError('cria_jogada: argumentos invalidos')
    jogada = (coordenada,inteiro)
    return jogada # para definir jogada temos de definir tabuleiro 
# fim cria_jogada #

#____________________Selectores______________________
def jogada_coordenada(jogada):
    if not e_jogada:
        raise ValueError('jogada_coodernada: argumentos invalidos')
    return jogada[0]
# fim jogada_coordenada #

def jogada_valor(jogada):
    if not e_jogada:
        raise ValueError('jogada_valor: argumentos invalidos')
    return jogada[1]
# fim jogada_valor #

#____________________Reconhecedores________________________

def e_jogada (universal):
    try:
        coordenada=universal[0]
        inteiro=universal[1]
        if not(e_coordenada(coordenada) and 0< inteiro<= 2):
            return False
    except(IndexError,TypeError,NameError,ValueError):
        return False 
    return True 
# fim e_jogada #

def jogadas_iguais (jog1,jog2):
    if not (e_jogada(jog1) and e_jogada(jog2)):
        return False 
    if not (\
            jogada_coordenada(jog1)==jogada_coordenada(jog2)\
            and jogada_valor(jog1)==jogada_valor(jog2)):              
        return False 
    
    return True 
# fim jogadas_iguais #

#_______________________________Transformadores___________________________________

def jogada_para_cadeia(jogada):  #tem de retornar "coordenada --> valor" 
    coordenada = jogada_coordenada(jogada)
    valor = jogada_valor(jogada)
    return str(str(coordenada_para_cadeia(coordenada))+ " --> " + str(valor))
# fim jogada_para_cadeia #



#_______________________________Funcoes Auxiliares_________________________________
def le_tabuleiro(string):
    ''' recebe uma string que é um nome de um ficheiro com os dados da 
    especificacao e devolve o tuplo das especificacoes'''
    ficheiro=open(string,"r")
    especificacoes = eval (ficheiro.readline())
    return especificacoes
# fim le_tabuleiro #




def pede_jogada(tabuleiro):
    ''' tabuleiro -> jogada
    recebe o tabuleiro do jogo e devolva a jogada que o jogador quer executar'''
#recebe os inputs da jogada 
    string = input ('Introduza a jogada\n- coordenada entre (1 : 1) e '+\
                    coordenada_para_cadeia(tabuleiro_dimensoes(tabuleiro))+' >> ')
    valor = int(input ("- valor >> "))

# avalia o input 
    coordenadas = eval(string.replace(":",","))
    coordenada = cria_coordenada(int(coordenadas[0]),int(coordenadas[1]))

# verifica a avaliacao do input 
    if not (e_coordenada(coordenada) and\
            coordenada[0]<= coordenada_linha(tabuleiro_dimensoes(tabuleiro)) and\
            coordenada[1]<= coordenada_coluna(tabuleiro_dimensoes(tabuleiro))\
            ):
        return False 
    return cria_jogada(coordenada,valor)
# fim pede_jogada #


#______________________________ Funcao Principal ______________________
def jogo_picross (string):
    '''funcao que permite jogar o jogo picross, completo,
        argumento: string com o nome do ficheiro
        devolve: True quando o jogo estevir completo, False caso contrario'''
    print('JOGO PICROSS')
    especificacoes = le_tabuleiro(string)
    tabuleiro = cria_tabuleiro(especificacoes)
    escreve_tabuleiro(tabuleiro)
    jogada_anterior = 0 
    
# enquanto o tabuleiro nao estiver completo jogamos
    while not (tabuleiro_completo(tabuleiro)):
        try:
            jogada = pede_jogada(tabuleiro)
            
            if not e_jogada(jogada):
                    print('Jogada invalida.')
# aplicar mudanca caso possivel                 
            if not (jogadas_iguais(jogada, jogada_anterior)) and e_jogada(jogada):
                    jogada_anterior=jogada 
                    tabuleiro_preenche_celula(tabuleiro, jogada_coordenada(jogada),jogada_valor(jogada))
            
        except(ValueError):
            print ('Jogada invalida.')

        escreve_tabuleiro(tabuleiro)
        if (tabuleiro_preenchido(tabuleiro)) and not (tabuleiro_completo(tabuleiro)):
            print('JOGO: O tabuleiro nao esta correto!')
            return False

    print ('JOGO: Parabens, encontrou a solucao!')
    return True 
#fim jogo_picross



#jogo_picross("jogo5x5.txt")



'''T = cria_tabuleiro(le_tabuleiro("jogo_fig2.txt"))
J = pede_jogada(T)
print("Introduza uma jogada*")
print("coordenada entre (1 : 1) e (5 : 5)) >> (1 : 5)*")
print("- valor >> 2*")
print(jogada_para_cadeia(J))
print("(1 : 5) --> 2*")
print(pede_jogada(T))
print("Introduza uma jogada*")
print("- coordenada entre (1 : 1) e (5 : 5)) >> (6 : 6)*")
print("- valor >> 2*")
print("False")
J = pede_jogada(T)
print("Introduza uma jogada*")
print("coordenada entre (1 : 1) e (5 : 5)) >> (5 : 5)*")
print("valor >> 2*")
print(jogada_para_cadeia(J))
print("5 : 5) --> 2*")'''



#------------------------------------------------------------------------
########################################################################################
#                                      Testes
########################################################################################

#pepe sucks 
# https://docs.python.org/2/library/stdtypes.html#string-formatting
#escreve_tabuleiro(cria_tabuleiro((((2, ), (3, ), (2, ), (2, 2), (2, )), ((2, ), (1, 2), (2,3,4,5,6,7 ), (3, ), (3, )))))

'''e=(((2,), (3,), (2,), (2, 2), (2,)), ((2,), (1, 2), (2,), (3,), (3,)))
t = cria_tabuleiro(e)
tabuleiro_dimensoes(t)
print("(5, 5)")
print(tabuleiro_especificacoes(t))
print("(((2,), (3,), (2,), (2, 2), (2,)), ((2,), (1, 2), (2,), (3,), (3,)))")
escreve_tabuleiro(t)
t1 = tabuleiro_preenche_celula(t, cria_coordenada(4, 2), 2)
escreve_tabuleiro(t)
print(tabuleiros_iguais(t, t1))
print("true")
t2 = tabuleiro_preenche_celula(t, cria_coordenada(4, 3), 1)
escreve_tabuleiro(t)
print(tabuleiros_iguais(t, t1))
print("true")
print(tabuleiros_iguais(t, t2))
print("true")
print(tabuleiro_celula(t, cria_coordenada(4, 1)))
print("0")
print(tabuleiro_celula(t, cria_coordenada(4, 2)))
print("2")
print(tabuleiro_celula(t, cria_coordenada(4, 3)))
print("1")
print(e_tabuleiro(t))
print("true")
print(e_tabuleiro("a"))
print("false")
print(tabuleiro_completo(t))
print("false")
t2 = tabuleiro_preenche_celula(t, cria_coordenada(1, 1), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(1, 2), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(1, 3), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(1, 4), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(1, 5), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(2, 1), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(2, 2), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(2, 3), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(2, 4), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(2, 5), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(3, 1), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(3, 2), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(3, 3), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(3, 4), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(3, 5), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(4, 1), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(4, 4), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(4, 5), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(5, 1), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(5, 2), 2)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(5, 3), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(5, 4), 1)
t2 = tabuleiro_preenche_celula(t, cria_coordenada(5, 5), 1)
escreve_tabuleiro(t)
print(tabuleiro_completo(t))
print("true")
escreve_tabuleiro(cria_tabuleiro((((1,),(3,),(1,)),((3,),(1,),(1,)))))'''


#J = cria_jogada(cria_coordenada(1, 1), 2)
#print(jogada_para_cadeia(J))
#print(coordenada_para_cadeia(jogada_coordenada(J)))
#print(jogada_valor(J))
#print(e_jogada(0))
#print(e_jogada(J))
#J2 = cria_jogada(cria_coordenada(1, 1), 1)
#print(jogadas_iguais(J, J2))
#J2 = cria_jogada(cria_coordenada(1, 1), 2)
#print(jogadas_iguais(J, J2))

