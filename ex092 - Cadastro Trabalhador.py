"""
NOME, ANO DE NASCIMENTO E CARTEIRA TRABALHO
O ano entra como idade no dicionario
caso a CTPS for diferente de zero, adicionar ano contratacao e salario
calcule com quantos anos ira se aposentar

from datetime import datetime
ano = datetime.now().year
"""

import datetime
cadastro = {}
anoatual=(datetime.date.today().year)
idade=aposentadoria=0

cadastro['nome'] = str(input('Nome: ')).title()
cadastro['nascimento'] = int(input('Ano de nascimento: '))
idade=anoatual-cadastro['nascimento']

cadastro['carteira'] = int(input('Carteira de trabalho [0 não tem]: '))
if (cadastro["carteira"]) > 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Último salário: '))
print()
print('<==== RESULTADO ====>')
print(f'Nome tem o valor...: {cadastro["nome"]}.')
idade=2020-cadastro['nascimento']
print(f'Idade tem  valor...: {idade}.')
if (cadastro["carteira"]) > 0:
    #cadastro['contratacao'] = int(input('Ano de contratação: '))
    print(f'CTPS é o número....:  {cadastro["carteira"]}.')
    print(f'Contratação foi ano: {cadastro["contratacao"]}.')
    print(f'Último salário   R$: {cadastro["salario"]:.2f}.')
    aposentadoria=idade+(35-(anoatual-(cadastro['contratacao'])))
    print(f'Aposentadoria é na idade {aposentadoria}.')

