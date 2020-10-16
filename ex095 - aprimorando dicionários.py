"""
Aprimore o exercicio 93
Varios jogadores
detalhes de aproveitamento
"""

time=[]
jogador={}
partidas=[]
cont=0

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(1,tot+1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO')
    if resp == 'N':
        break
print('-'*40)

print('cod ', end= '')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)


for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):15}', end='')
    print()
print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe esse jogador')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'      No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')




"""

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1} fez {v} gols ')

print('-='*30)

"""