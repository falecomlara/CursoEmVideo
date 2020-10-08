# um ano qualquer é bissexto
ano = int(input('Que ano estamos? '))
biano = ano % 4
print('{} é bissexto'.format(ano) if biano == 0 else '{} não é bissexto'.format(ano) )