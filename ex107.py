#Crie um módulo chamado moeda.py que tenha funçòes incorporadas
#- aumentar(), diminuir(), dobro() e metade()
#faça um programa que importe estes dados e faça uso das funções

import moeda

p = float(input('Digite o preço: R$ '))
print('-='*12)
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro  de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo  15%, temos R${moeda.diminuir(p, 15)}')