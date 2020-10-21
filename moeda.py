# Módulo MOEDA utilizado nos exercícios 107 - 111

#from decimal import Decimal

def aumentar(num=0, porcento=0, form=False):
    """

    :param num:  é um valor inteiro ou float (preço do produto)
    :param porcento: é a porcentagem a ser aplicada
    :param form: FALSE não é formatado, TRUE, é formatado com virgulas
    :return:
    """
    res = (num+(num*(porcento/100)))
    return res if form is False else virgula(res)


def diminuir(num=0, porcento=0, form=False):
    res = (num-(num*(porcento/100)))
    return res if form is False else virgula(res)


def dobro(num=0, form=False):
    res = (num*2)
    return res if form is False else virgula(res)


def metade(num=0, form=False):
    res = (num/2)
    return res if form is False else virgula(res)


def virgula(num=0, sigla='R$'):
    return f'{sigla}{num:.2f}'.replace('.', ',')


def titulo(msg):
    print('-' * 32)
    print(f'{msg:^30}')
    print('-' * 32)


def resumo(num=0, taxaAumentar=10, taxaReduzir=5):
    """
    ==> Retorna tabela formatada
    :param num: Preço (INT) a ser validado
    :param taxaAumentar: Porcentagem (INT) que será aumentada
    :param taxaReduzir:  Porcentagem (INT) que será diminuido
    :return:
    """
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado: \t\t{virgula(num)}')  # Aqui usei três tabulações
    print(f'Dobro do preço: {dobro(num, True):>17}') # Aqui usei :>17 para direita
    print(f'Metade do preço: \t\t{metade(num, True)}')
    print(f'{taxaAumentar}% de aumento: \t\t{aumentar(num, taxaAumentar, True)}')
    print(f'{taxaReduzir}% de redução: \t\t\t{diminuir(num, taxaReduzir, True)}')
    print('-' * 32)



