# CONDICOES ANINHADAS (uma coisa dentro de outra)
'''
x = 2
if x==2:
    print(x)
elif x==3:
    print(x)
elif x==4:
    print(x)
else:
    print(x)
'''

nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito, {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil, {}'.format(nome))
elif nome in 'Ana Jessica Andreia':
    print('Seu nome é bonito, {}'.format(nome))
else:
    print('Seu nome é bem normal. Tenha um bom dia, {}'.format(nome))