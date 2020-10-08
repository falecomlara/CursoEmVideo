'''
cpu jogar jokenpo
'''
mensagem = 'JOKENPO'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

import random, time

cpu = random.randrange(1,3)

voce = int(input('''[1] PEDRA
[2] PAPEL
[3] TESOURA
SUA ESCOLHA: '''))
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)


print('-=-'*7)
if voce == 1 and cpu == 1:
    print('VC:Pedra, CPU:Pedra')
    print('EMPATE')
    print('-=-' * 7)

elif voce == 2 and cpu == 2:
    print('VC:Papel, CPU:Papel')
    print('EMPATE')
    print('-=-' * 7)

elif voce == 3 and cpu == 3:
    print('VC:Tesoura, CPU:Tesoura')
    print('EMPATE')
    print('-=-' * 7)

elif voce == 1 and cpu == 2:
    print('VC:Pedra, CPU:Papel')
    print('Você perdeu!')
    print('-=-' * 7)

elif voce == 1 and cpu == 3:
    print('VC:Pedra, CPU:Tesoura')
    print('Você ganhou!')
    print('-=-' * 7)

elif voce == 2 and cpu == 1:
    print('VC:Papel, CPU:Pedra')
    print('Você perdeu!')
    print('-=-' * 7)

elif voce == 2 and cpu == 3:
    print('VC:Papel, CPU:Tesoura')
    print('Você perdeu!')
    print('-=-' * 7)

elif voce == 3 and cpu == 1:
    print('VC:Tesoura, CPU:Pedra')
    print('Você perdeu!')
    print('-=-' * 7)

elif voce == 3 and cpu == 2:
    print('VC:Tesoura, CPU:Papel')
    print('Você ganhou!')
    print('-=-' * 7)

else:
    print('OPÇÃO INVÁLIDA')
    print('-=-' * 7)