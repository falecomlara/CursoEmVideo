#Melhorar o ex107, criando uma funçõa adicional chamada moeda()
#que consiga mostrar os valores como um valor formatado como moeda

#DICA talvez importando o DECIMAL

import moeda

p = float(input('Digite o preço: R$ '))
print('-='*12)
print(f'A metade de {moeda.virgula(p)} é {moeda.virgula(moeda.metade(p))}')
print(f'O dobro  de {moeda.virgula(p)} é {moeda.virgula(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.virgula(moeda.aumentar(p, 10))}')
print(f'Reduzindo  15%, temos {moeda.virgula(moeda.diminuir(p, 15))}')

