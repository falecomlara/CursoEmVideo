#LISTAS COMPOSTAS (listas dentro de listas)

""" Básico sobre listas
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) # PEDRO
print(dados[1]) # 25
"""

#Listas Compostas

"""
pessoas = list()
pessoas.append('Eduardo')
pessoas.append(pessoas[:])
print(pessoas)
print('-=-'*20)
"""

#Posicionamento de Elementos dentro de uma Lista Composta
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
#print(pessoas[0][0]) # Dentro da lista Zero, retorna o Valor na posição Zero = Pedro
#print(pessoas[1][1]) # Dentro da lista Um, retorna o valor na posição Um = 19
#print(pessoas[1])
pessoas.append(['Eduardo',18])
print(pessoas[3])

"""
pessoas = list()
pessoas.append('Gustavo')
pessoas.append(40)
galera = list()
galera.append(pessoas[:])
print(galera)
pessoas[0]='Maria'
pessoas[1]=22
galera.append(pessoas)
print(galera)
"""


galera=list()
dado=list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome.: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Aqui ele faz uma cópia de DADO
    dado.clear()
print(f'A galera é {galera}')
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        totmaior+=1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor+=1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')
