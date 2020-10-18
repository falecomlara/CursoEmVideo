#Função chamada VOTO que vai receber o ano de nascimento.
#Retornando o valor literal, indicando se uma pessoa tem voto
#NEGADO, OPCIONAL ou OBRIGATORIO

from datetime import datetime
ano = datetime.now().year # essa é uma variável global
nascimento=0

def voto(nascimento=0):
    idade=ano-nascimento
    if idade >=18 and nascimento != 0:
        print(f'Com {idade} anos: Voto Obrigatório')
    elif idade >=16 and nascimento!=0:
        print(f'Com {idade} anos: Voto Opcional')
    elif idade <16:
        print(f'Com {idade} anos: Voto NEGADO')
    else:
        print(f'Nenhum valor informado')

"""
voto(1974)
voto(1984)
voto(1994)
voto(2000)
voto(2004)
voto(2010)
voto(2014)
voto()
"""

nascimento=int(input('Em que ano você nasceu? '))
voto(nascimento)