#Utilizando Módulos
'''
Ilustração: O corpo, que precisa ter acesso a bebida, comida, doce.
Então eu faço o "IMPORT bebida" ou "IMPORT comida".
Mas e se eu quiser importar apenas o Pudim, do módulo doce?
Então utilizo o "FROM doce IMPORT pudim"

import math (aqui está importando tudo)
from math import sqrt, ceil (aqui importa apenas dois módulos)
'''

"""
import math, random
# num = int(input('Digite um número: '))
num = random.randrange(1,100,1)
raiz = math.sqrt(num) #pedi para usar uma função
print('A raiz de {} é {}'.format(num, math.ceil(raiz))) #fiz arredondamento com o ceil
"""

import emoji
print(emoji.emojize('Olá Mundo :earth_americas:', use_aliases=True))