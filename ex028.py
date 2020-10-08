# pensar número entre 0-5 e tenta adivinhar
import random
from time import sleep
cpu = random.randrange(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 e 5. Tente adivinhar...')
print('-=-'*20)
sleep(1)
user = int(input('Que número pensei? '))
print('PROCESSANDO...')
sleep(3)
print('PARABÉNS! Você conseguiu me vencer!' if user == cpu else 'ERROU, eu pensei em {}'.format(cpu))