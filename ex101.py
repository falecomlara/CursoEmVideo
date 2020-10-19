#Função chamada VOTO que vai receber o ano de nascimento.
#Retornando o valor literal, indicando se uma pessoa tem voto
#NEGADO, OPCIONAL ou OBRIGATORIO

""" Outro exemplo de pedir o ano
from datetime import date
atual = date.today().year
"""


def voto(ano=0):
    from datetime import datetime #importar dentro da função, economiza memória
    atual = datetime.now().year  # essa é uma variável local
    idade= atual - ano
    if idade < 16:
        print(f'Com {idade} anos:\033[0:31:40m Voto NEGADO \033[0:0:0m')
    elif 16 <= idade < 18 or idade > 65 and ano != 0:
        print(f'Com {idade} anos:\033[0:31:33m Voto Opcional \033[0:0:0m')
    elif idade >=18 and idade <= 65 :
        print(f'Com {idade} anos:\033[0:31:32m Voto Obrigatório \033[0:0:0m')
    else:
        print(f'\033[0:31:34mNenhum valor informado \033[0:0:0m')


print('-='*10)
print(' SISTEMA DE VOTAÇÃO')
print('-='*10)

voto(1954)
voto(1955)
voto(1974)
voto(1984)
voto(2002)
voto(2003)
voto(2004)
voto(2005)
voto(2014)
voto()

# Exemplo de input do ano, na função:
# nascimento=int(input('Em que ano você nasceu? '))
# voto(nascimento)
