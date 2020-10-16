# 15-outubro-2020
# JOGO QUE DESENVOLVI PARA TESTAR LISTAS COMPOSTAS

import random
from time import sleep

jogadores = []
temporario = []
nome1 = nome2 = ''
hp1 = hp2 = 0
forca1 = forca2 = 0
cont = 1
round = 0

while cont <= 2:
    nome = str(input(f'Jogador {cont}: ')).title()
    hp = random.randrange(10, 50)
    forca = random.randrange(5, 10)
    jogadores.append([nome, [hp, forca]])
    cont += 1
print('-=' * 20)
print(f'{jogadores[0][0]} <VS> {jogadores[1][0]}')

nome1 = (jogadores[0][0])  # player 1
hp1 = (jogadores[0][1][0])  # HP1
forca1 = (jogadores[0][1][1])  # força

nome2 = (jogadores[1][0])  # player2
hp2 = (jogadores[1][1][0])  # HP2
forca2 = (jogadores[1][1][1])  # força

# print(f'STATUS {nome1} hp {hp1} forca {forca1}')
# print(f'STATUS {nome2} hp {hp2} forca {forca2}')

while True:
    round += 1
    print(f'Round {round}: ', end='')
    # print(f'{jogadores[0][0]} ataca {jogadores[1][0]}')
    n = random.randint(1, 5)
    sleep(1)
    if n == 1:
        sleep(1)
        print(f'{nome1} acertou com força {nome2}')
        sleep(1)
        print('BANG!! , BOOM!!')
        sleep(1)
        print(f'HP: {hp2}', hp2 * '#')
        sleep(1)
        hp2 = hp2 - forca1
        print(f'HP: {hp2}', hp2*'#')
        if hp1 <= 0:
            sleep(1)
            print('-=' * 20)
            print(f'{nome2} GANHOU A BATALHA APÓS {round} ROUNDS')
            break
        elif hp2 <= 0:
            sleep(1)
            print('-=' * 20)
            print(f'{nome1} GANHOU A BATALHA APÓS {round} ROUNDS')
            break

    if n == 2:
        sleep(1)
        print(f'{nome2} acertou com força {nome1}')
        sleep(1)
        print('BANG!! , BOOM!!')
        sleep(1)
        print(f'HP: {hp1}', hp1 * '#')
        sleep(1)
        hp1 = hp1 - forca2
        print(f'HP: {hp1}', hp1 * '#')

        if hp2 <= 0:
            sleep(1)
            print('-=' * 20)
            print(f'{nome1} GANHOU A BATALHA APÓS {round} ROUNDS')
            break
        elif hp1 <= 0:
            sleep(1)
            print('-=' * 20)
            print(f'{nome2} GANHOU A BATALHA APÓS {round} ROUNDS')
            break

    if n == 3:
        sleep(1)
        print(f'{nome1} tomou uma poção de ENERGIA ')
        sleep(1)
        print('Glup, glup, glup')
        sleep(1)
        print(f'HP: {hp1}', hp1*'#')
        hp1 += random.randrange(1, 6)
        sleep(1)
        print(f'HP: {hp1}', hp1*'#')
        sleep(1)

    if n == 4:
        sleep(1)
        print(f'{nome2} tomou uma poção de ENERGIA ')
        sleep(1)
        print('Ahh que refrescante')
        print( f'HP: {hp2}', hp2 * '#')
        hp2 += random.randrange(1, 6)
        sleep(1)
        print(f'HP: {hp2}', hp2 * '#')
        sleep(1)
    if n == 5:
        sleep(1)
        print(f'Eles ficaram se olhando')
        sleep(1)
        print('... e não fizeram nada.')

    print('-=' * 20)
print()
print('GAME OVER')
