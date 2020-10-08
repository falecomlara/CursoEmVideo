'''
ano nascimento, ano do sistema
vai ter de se alistar? (menor 17)
esta na hora de se alistar? (17-18)
já passou do tempo de se alistar? (19)
Quanto tempo falta? Já passou x anos
'''

import datetime

hoje = datetime.date.today().strftime("%Y")
# print(hoje.strftime("%d/%m/%Y"))

''' OUTRO MODO DE PEDIR O ANO
from datetime import date
ano = date.today().year
print (atual)
'''

mensagem = 'ALISTAMENTO MILITAR {}'.format(hoje)
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

nasceu = int(input('Que ano você nasceu? '))
idade = (int(hoje))-nasceu

#print('Você tem {} anos.'.format(idade))

if idade < 0 or idade > 100:
    print('ANO NASCIMENTO INVÁLIDO')
elif idade == 18:
    print('Você tem {} e estamos no ano ({}) do seu alistamento'.format(idade,hoje))
elif idade > 18:
    print('Você tem {} anos e já se passaram {} ano(s) do alistamento.'.format(idade,idade-18))
else:
    print('Você tem {} anos e faltam {} ano(s) para se alistar.'.format(idade,18-idade))