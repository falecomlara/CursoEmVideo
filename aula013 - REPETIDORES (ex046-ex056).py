#REPETIDORES, Laços (com variável de controle), Iterações
"""
laco C no intervalo (1,10):
  se moeda = True
    pega
  passo
passo
pega
"""

''' EXEMPLO 
for c in range (1,3):
    print ('Indo', c)
print('fim')

for c in range (3,0,-1):
    print ('Voltando', c)
print('fim')
'''

''' EXEMPLO INSERINDO NUMERO
n = int(input('Digite um número: '))
for c in range (1,n+1):
    print ('Indo', c)
print('fim')

for c in range (n,0,-1):
    print ('Voltando', c)
print('fim')
'''

# Exemplo de somatório usando laço
s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n
    print('Valor atual é {}'.format(s))
print('O somatório de todos os valores foi {}'.format(s))