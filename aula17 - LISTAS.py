""" INTRODUÇÃO LISTAS (Elas são mutáveis)
(TUPLAS), [LISTAS]
"""
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print('lista:',lanche)
lanche[3]='picolé'
print('posição:', lanche)
lanche.append('Cookie')
print('append:', lanche)
lanche.insert(0, 'cachorro-quente')
print('insert:', lanche)
lanche.pop(0)
print('pop(0):', lanche)
lanche.remove('pizza')
print('remove:', lanche)
del lanche[0]
print('del[0]:', lanche)
# usando IF
#if pizza in lanche:
#    lanche.remove('pizza')
#print(lanche)

valores = list(range(0,11)) # inicia 4 e termina no 10, gera uma lista
print('Uso range', valores)
valores.sort(reverse=True)
print('Sorted reverso', valores)
print(len(valores))

print('-=-'*20)

num1 = (2,5,9,1)
num2 = [2,6,9,1,2,5]
print(num1, type(num1), '<-  tuplas são imutáveis')
print(num2, type(num2), '<-  listas são mutáveis')
print(f'Essa lista tem {len(num2)} elementos')
num2.insert(2,0)
print(num2, type(num2), '<- insert(2,0)')
print(f'Essa lista tem {len(num2)} elementos')
num2.pop(1)
print(num2, type(num2), '<- pop(1)')
print(f'Essa lista tem {len(num2)} elementos')
print(num2, type(num2), '<- remove(2)')
if 2 in num2:
    num2.remove(2)
else:
    print('não achei o número 5')
print(f'Primeira ocorrência do 2, removido', num2)

print('-=-'*20)

valores = []
valores.append(3)
valores.append(5)
valores.append(9)

print(valores)
for v in valores:
    print(f'{v}...', end='')

print(f'\n', '-=-'*20)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')

print('-=-'*20)

"""
numeros = []
for contador in range (0,5):
    numeros.append(int(input('Digite um valor: ')))

for c, v in enumerate(numeros):
    print(f'Na posição {c} entrou o valor {v}!')
print('Fim da lista usando Input')
"""

a = [2,3,4,6]
b = a
c = a[2:]
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C na posição [2:] em diante: {c}')
b[2] = 8
print(f'Adiciona 8 na posição [2] {b} ')