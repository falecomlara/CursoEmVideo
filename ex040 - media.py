'''
duas notas:
media abaixo de 5.0 < reprovado
media entre 5.0 e 5.9 = recuperacao
media 6.0 = aprovado
'''
mensagem = 'MÉDIA DE NOTAS'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota.: '))

media = (n1+n2)/2
if media < 5:
    print('Sua média foi de {}'.format(media))
    print('REPROVADO')
elif media >= 5 and media < 6:
    print('Sua média foi de {}'.format(media))
    print('RECUPERAÇÃO')
else:
    print('Sua média foi de {}'.format(media))
    print('APROVADO')