# nome, idade e sexo de 04 pessoas
# media da idade
# nome do homem mais velho
# quantas mulhers menos de 21 anos

somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher = 0

for p in range (1,4):
    print('---{}ª pessoa ---'.format(p))
    nome  = str(input('Nome: '.format(p)))
    idade = int(input('Idade: '.format(p)))
    sexo  = str(input('Sexo [M/F]: ').upper())
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehome:
        maioridadehome =idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher += 1

mediaidade = somaidade / p
print('media do grupo ', round(mediaidade),2)
print(maioridadehome, nomevelho)
print(totmulher)
