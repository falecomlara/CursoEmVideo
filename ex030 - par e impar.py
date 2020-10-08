# digita um numero e descubra se é par ou impar
import random
numero = random.randrange(0,100)
resultado = numero % 2
print('{} é PAR'.format(numero) if resultado == 0 else '{} é IMPAR'.format(numero))