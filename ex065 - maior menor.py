# leia varios numeros
# no final mostre a media?
# qual o maior? qual foi o menor?
# continuar [S/N]?

#Solução exercício
resp = 'S'
soma = qtde = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtde += 1
    if qtde == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma/qtde

print('Você digitou {} e a media foi {}'.format(num,media))
print('O maior foi {} e o menor foi {}'.format(maior,menor))
print('acabou')


""" ESSE EU FIZ, mas esta dando erro na media
num1 = 0
num2 = 0
sair = ''
digitou = 1
media = 0
maior = 0
menor =0
x=0
y=0

num1 = int(input('Digite um número: '))
while sair != 'N':
    sair = str(input('Quer continuar? [S/N] ')).upper().strip()
    if sair == 'S':
        num2 = int(input('Digite um número 2: '))
        digitou += 1
        media = (num1+num2)
        x=num1
        y=num2
        #num1 = media

        if y > x or x < y:
            maior = y
            menor = x
        if y < x or x > y:
            menor = y
            maior = x
        if y == x or x == y:
            maior = x
            menor = y
print ('Você digitou {} números, a média foi {}, o maior é {} e o menor é {}.'.format(digitou,media/2,maior,menor))
"""