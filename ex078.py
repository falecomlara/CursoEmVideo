#leia cinco valores numericos em uma lista
# usar for range
# no final mostrar qual o valor maior e o menor valor valores
# e suas respectivas posições na lista

valores = []
maior=menor=0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c==0:
        maior = menor = valores[c]
    else:
        if valores[c]>maior:
            maior=valores[c]
        if valores[c]<menor:
            menor=valores[c]
print('-=-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()


""" Meu exercício:

c = 1
valores =[]

num = (int(input(f'Digite um valor para a posição 1: ')))
maior = menor = num
valores.insert(c, num)

for c in range(2,6):
    num = (int(input(f'Digite um valor para a posição {c}: ')))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    valores.insert(c, num)
print(f'Você digitou os valores {valores}')
indicemaior = valores.index(maior)
indicemenor = valores.index(menor)
valores.sort()
print('-=-'*10)
print(f'O MAIOR valor digitado foi o {valores[-1]} na posição {indicemaior+1}.')
print(f'O MENOR valor digitado foi o {valores[0]} na posição {indicemenor+1}.')
"""