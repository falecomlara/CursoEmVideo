'''
ler cada valor em um teclado
guardar em uma tupla
quantas vezes apareceu o nove?
em que posicao foi digitado o primeiro valor 3
quais foram os numeros pares.
'''

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um último número: '))) # Criou uma TUPLA em NUM

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição.')
else:
    print('O valor 3 não apareceu em nenhuma posicao')
print(f'Os números pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


''' Minha solução
cont = num = 0
lista = []
pares = []
while cont < 4:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont +=1
    if num % 2 == 0:
        pares.append(num)
tupla = tuple(lista)

print('Você digitou os números: ', lista)

print(f'O valor 9 apareceu {lista.count(9)} vezes')
print(f'O valor 3 apareceu {lista.index(3)+1} posição')
print(f'Os números pares digitados {pares}')
'''
