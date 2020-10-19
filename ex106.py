#Mini Sistema Interactive Help
#FIM ele encerra

#40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(ciano), 47(cinza)

from time import sleep


c = ('\033[0;0m',     # 0 remove formatação
                      #   FONTE  FUNDO
     '\033[0;30;40m', # 1 preto, preto
     '\033[0;30;41m', # 2 preto, vermelho
     '\033[0;30;42m', # 3 preto, verde
     '\033[0;30;43m', # 4 preto, amarelo
     '\033[0;30;44m', # 5 preto, azul
     '\033[0;30;45m', # 6 preto, roxo
     '\033[0;30;46m', # 7 preto, ciano
     '\033[0;30;47m', # 8 preto, cinza
     '\033[1;30;107m' # 9 preto, branco
     )


def titulo(msg, cor=0):
    """
    ==> TITULO PERSONALIZADO
    :param msg: A mensagem que você deseja imprimir
    :param cor: O número da cor em c[x]
    :return:
    """
    tam = len(msg) + 4
    print(c[cor], end='')
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)
    print(c[0], end='')

def ajuda(comando=0):
    """
    ==> Função do comando
    :param comando: O comando do help
    :return:
    """
    while True:
        if comando.upper() == 'FIM':
            break
        else:
            print(c[9])
            help(comando)
            sleep(1)
            print(c[0])
            comando = str(input('Função ou Biblioteca: (FIM encerra) '))


#INICIO DO PROGRAMA
#comando = ''
titulo('SISTEMA DE AJUDA', 3)
comando = str(input('Função ou Biblioteca: (FIM encerra) '))
ajuda(comando)
titulo('ATÉ LOGO', 2)
