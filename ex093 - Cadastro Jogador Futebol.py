"""
NOME DO JOGADOR
QUANTAS PARTIDAS ELE JOGOU
- QUANTIDADE DE GOLS
Total de gols do campeonato
"""
# Solução do Curso


jogador={}
partidas=[]
cont=0
jogador['nome'] = str(input('Nome do jogador: ')).title()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(1,tot+1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1} fez {v} gols ')

print('-='*30)

