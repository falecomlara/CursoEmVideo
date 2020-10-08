nome = input('Qual o seu nome completo? ')
if nome.__contains__('Silva'):
    print('Seu nome {} contém Silva'.format(nome))
else:
    print('Seu nome {} não contém Silva'.format(nome))