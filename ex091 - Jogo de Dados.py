"""
QUATRO JOGADORES TEM UM DADO
GUARDE TODOS OS VALORES EM UM DICIONARIO
COLOQUE ESSE DICIONARIO EM ORDEM
VENCEDOR TIROU O MAIOR NUMERO DO DADO
"""
import random
from time import sleep

resultados={} #dicionario
jogo=[] #lista
dado=lugar=0
for c in range(1,5):
    dado = random.randrange(1, 7)
    resultados[f'Jogador{c}'] = dado
    jogo.append(jogo.copy())

print('VALORES SORTEADOS')
for c,v in resultados.items():
    sleep(1)
    print(f'O jogador {c}, tirou {v}')

print()

print('RANKING DE JOGADORES')
for c,v in sorted(resultados.items(), reverse=True, key=lambda x:x[1]):
    lugar+=1
    sleep(1)
    print(f'Em {lugar}° lugar: {c} com {v}. ')

#fonte para ordenar valores reverso dicionários:
#https://dzone.com/articles/sorting-dictionaries-in-python

"""
Uma outra maneira de ordenar os dados é:
from operator import itemgetter
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
"""