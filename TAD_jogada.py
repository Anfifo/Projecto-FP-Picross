def cria_jogada(coordenada, inteiro):
    if not (e_coordenada(coordenada) and inteiro>0 and inteiro <=2):
        raise ValueError('cria_jogada: argumentos invalidos')
    return jogada # para definir jogada temos de definir tabuleiro 

def jogada_coordenada(jogada):
    return #coordenada da jogada (incompleta)

def jogada_valor(jogada):
    return #valor da jogada (incompleta)

def e_jogada (x):
    return #condicao que defina uma jogada (incompleta)

def jogadas_iguais (jog1,jog2):
    if jog1==jog2:              #se forem iguais e verdadeira
        return True
    else: 
        return False

def jogada_para_cadeia(jogada):  #tem de retornar "coordenada --> valor" 
    coordenada = jogada_coordenada(jogada)
    valor = jogada_valor(jogada)
    return str(coordenada_para_cadeia(coordenada)+ "-->" + valor) 
