'''
entrada da idade do atleta
9 anos = mirim
14 = infantil
19 = junior
25 = senior
acima = master
'''

from datetime import date
ano = date.today().year

mensagem = 'CLASSIFICAÇÃO DOS ATLETAS : {}'.format(ano)
traco = len(mensagem)
print ('*'*traco)
print(mensagem)
print ('*'*traco)

nasceu = int(input('Ano de nascimento? '))
idade = ano - nasceu

if idade <= 0 or idade >= 100:
    print('ANO NASCIMENTO INVÁLIDA')
elif idade <= 9:
    print('Atleta tem {} anos.'.format(idade))
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Atleta tem {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Atleta tem {} anos.'.format(idade))
    print ('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Atleta tem {} anos.'.format(idade))
    print ('Classificação: SENIOR')
else:
    print('Atleta tem {} anos.'.format(idade))
    print ('Classificação: MASTER')