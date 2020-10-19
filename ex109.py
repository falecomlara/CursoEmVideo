#Melhore o desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela
#função moeda()


import moeda

p = float(input('Digite o preço: R$ '))
print('-='*12)
print(f'A metade de {(p)} é {metade(p, True)}')
print(f'O dobro  de {(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo  15%, temos {diminuir(p, 15, True)}')