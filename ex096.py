#FUNÇÃO CHAMADA AREA, que receba dimensoes de um terreno (largura x comprimento)
#e mostre a area do terreno

def calculararea(largura, comprimento):
    """
    -> Faz o cálculo
    :param largura: É a largura da sala
    :param comprimento: É o comprimento da sala
    :return: Ele irá calcular e retornar a área da sala
    Função criada por Eduardo Lara no curso de Python.
    """
    area=largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m.')


#INICIO DO PROGRAMA
#print('CÁLCULO DE TERRENOS')
#print('-'*19)
#largura = float(input('Largura (m): '))
#comprimento = float(input('Comprimento (m):  '))

calculararea(largura, comprimento)

