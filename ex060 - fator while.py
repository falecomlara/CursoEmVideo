# leia numero qualquer e mostra o fatorial
# 5!= 5x4x3x2x1 = 120 (multiplica de frente para tras ate dar o valor)

"""" modo SUPER SIMPLES
from math import factorial
n = int(input('Entre com um número '))
f = factorial(n)
print('O fato de {}, é {}.'.format(n, f))
"""

# Solução Aula
n = int(input('Entre com um número '))
c = n
f = 1
print ('Calculando {}! = '.format(n), end='')
while c > 0:
    print ('{}'.format(c), end='')
    print (' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print ('{}'.format(f))



""" Modo SUPER AVANÇADO
fator = int(input('Entre com um número: '))
x = fator
y = fator
soma = 0
print('Fator de {} = '.format(fator), end='')
print(x, end='')

while fator != 1:
    print(' x ', end='')
    print(y - 1, end='')
    x = (x * (y - 1))
    soma = x + soma
    y = y - 1
    fator = fator - 1  # termina o laço
print(' = {} '.format(x))
"""