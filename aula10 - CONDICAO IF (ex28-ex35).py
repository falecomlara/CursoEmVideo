# Condições Simples e Composto

'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
'''
#CONDIÇÃO SIMPLIFICADA
# print('carro novo' if tempo <=3 else 'carro velho')

'''
nome = str(input('Qual o seu nome? ')).upper()
if nome == 'EDUARDO':
    print('Que nome lindo você tem {}'.format(nome))
else:
    print('Seu nome {} é tão normal. Bom dia.'.format(nome))
'''

nota1 = float(input('Digite primeira nota: '))
nota2 = float(input('Digite primeira nota: '))
n = (nota1+nota2)/2
print('sua media {} foi boa'.format(n) if n>=6 else 'sua nota {} não foi boa'.format(n))