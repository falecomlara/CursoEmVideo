# Exercício 24 - digite um nome de cidade e verifica se tem Santo

nome = input('Onde você nasceu? ')
if nome.startswith('Santo'):
    print('A cidade {} começa com a palavra Santo'.format(nome))
else:
    print('A cidade {} não começa com a palavra Santo'.format(nome))