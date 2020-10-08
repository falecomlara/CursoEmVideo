#pensar numero entre 0 e 10
# vai tentar adivinhar, até acertar, mostrando quantos palpites no final
import random
n = random.randrange(0,10)
palpite = 0
numero = 0

numero = int(input('De 0 a 10: Qual estou pensando?' ))
palpite += 1
while numero != n:
    while n > numero:
        print ('Mais que {}. Tente novamente.'.format(numero))
        numero = int(input('-> '))
        palpite += 1
    while n < numero:
        print ('Menos que {}. Tente novamente.'.format(numero))
        numero = int(input('-> '))
        palpite += 1
else:
    print('Eu pensei em {} e você acertou!'.format(n))
print('Foi preciso {} palpites'.format(palpite))

