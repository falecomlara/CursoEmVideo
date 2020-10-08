# tupla com 20 primeiros colocados (tabela brasileirao) na ordem colocacao
# apenas os 5 primeiros colocados (fatiamento)
# os ultimos 4
# lista de de A-Z
# que posicao esta o time Vasco

times = ('Atlético-MG','Internacional','Palmeiras','Flamengo','Sport','Santos',
         'São Paulo','Fluminense','Vasco','Fortaleza','Atlético-GO','Athletico-PR',
         'Ceará','Corinthians','Grêmio','Bahia','Coritiba','Bragantino','Botafogo','Goiás')

print('-=-'*10)
print(f'Lista de times do brasileirão: {times}')
print('-=-'*10)
print(f'Os 5 primeiros são..: {(times[0:5])}')
print('-=-'*10)
print(f'Os 4 últimos são....: {(times[-4:])}')
print('-=-'*10)
print(f'Em ordem alfabética.: {(sorted(times))}')
print('-=-'*10)
print('O time Vasco posição: ', times.index('Vasco')+1)

