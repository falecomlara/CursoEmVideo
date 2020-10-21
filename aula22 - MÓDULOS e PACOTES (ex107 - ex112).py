""" MÓDULOS
surgiu na decada 60 e os sistemas estavam ficando cada vez maiores
- foco dividir um programa
- aumentar a legibilidade
- facilitar a manutenção

 Vantagens Módulos:
- Organização do código
- Facilidade na manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos
"""

# Movimentar todas as DEF para um novo arquivo, chamado 'modulo022.py'
#Ao invés de usar as funções dentro do programa, eu crio um novo arquivo e o defino como módulo.

"""
def fatorial(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return  n*3
"""

# depois de gerado/criado o novo módulo, devo importar para o programa principal

import modulo022  #Importei o módulo que criei minhas funções.

#agora preciso adicionar o módulo, no caminho das requisições

#PROGRAMA PRINCIPAL
num=int(input('Digite um valor: '))
# fat=fatorial(num)                 #ANTES, quando a DEF está no programa principal
fat=modulo022.fatorial(num)         #DEPOIS, quando a DEF está no módulo criado
print(f'O fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {dobro(num)}')     #ANTES
# print(f'O dobro de {num} é {triplo(num)}')    #ANTES
print(f'O dobro de {num} é {modulo022.dobro(num)}')  #DEPOIS, usando o módulo criado
print(f'O dobro de {num} é {modulo022.triplo(num)}') #DEPOIS, usando o módulo criado

# Agora olhe que legal, poderia importar apenas uma ÚNICA função.

from modulo022 import dobro

print(f'Testando a importação DOBRO é {dobro(num)}') # E o comando muda para usar o módulo.
print()
# chamando HELP, direto da função.
print(help(dobro))

""" Os pacotes, são conjuntos de módulos:
Um programa é = { Pacotes [que contém Módulos (que contém suas funções) ] }

Para importar uso o nome direto:
- import modulo022
Ou posso importar apenas a função:
- from modulo022 import dobro

 Dentro do Python, para criar um pacote, crio uma pasta e dentro de cada pasta,
eu organizo o meu projeto

O nome de um pacote é '__init__.py'

Para criar o pacote:
1º Clique com o botão direito em cima da pasta principal e selecione NEW -> Python Package
2º Defina um nome da pasta
3º Um arquivo '__init__.py' será criado
4º E dentro de cada pasta, crie um módulo, com suas funções.