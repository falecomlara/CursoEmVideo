# DICIONÁRIOS - Variáveis Compostas
# Tuplas=(), Listas=[], Dicionários={}


dados = {'nome': 'Pedro', 'idade': 25}
print (dados['nome'], dados['idade'])
#ADICIONAR ELEMENTOS
dados['sexo']='M' #Dicionário dados, recebe SEXO, com elemento M
print(dados)
#REMOVER ELEMENTOS
del dados['idade']
print(dados)

# OUTRO EXEMPLO COM FILMES
filmes = {'titulo' : 'Star Wars',
          'ano'    : 1977,
          'diretor': 'George Lucas'
          }
print(filmes.values())
print(filmes.keys())
print(filmes.items())
print()

# Exemplo usando FOR
for chave, valor in filmes.items():
    print(f'O {chave} é {valor}. ')


pessoas ={'nome':'eduardo', 'sexo':'M', 'idade':30}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(type(pessoas))
print('')

for k,v in pessoas.items():
    print(f'{k} = {v}')
print('')

del pessoas['sexo']   # removi o SEXO
pessoas['nome'] = 'Leandro' # troquei o nome por Leandro
pessoas['peso'] = 98.5 # adicionei um novo campo PESO

for k,v in pessoas.items():
    print(f'{k} = {v}')
print('')

# AGORA colocar um DICIONARIO dentro de um LISTA

brasil=[]
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo'     , 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil, type(brasil)) # Exibe a lista
print(brasil[0])            # Exibe a lista 0
print(brasil[0]['uf'])      # Na lista 0, exibe a chave uf



estado={} #dicionario
brasil=[] #lista
for c in range (0,3): #três loops
    estado['uf']   =str(input('Unidade Federativa: ')).title()
    estado['sigla']=str(input('Sigla Estado: ')).upper()
    brasil.append(estado.copy()) # se fosse lista, seria: brasil.append(estado[:])
print(brasil)
print()

print('EXEMPLO DE UMA LAÇO')
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print()

print('EXEMPLO DE OUTRO LAÇO')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()