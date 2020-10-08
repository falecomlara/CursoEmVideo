#jogue par ou impar com o CPU
# o jogo só será interrompido se ele perder
# mostrar vitorias concecutivas

import random

par = impar = cont = soma = valor = escolheu = 0
vitoria = 'S'

print('VAMOS JOGAR PAR OU IMPAR')
while vitoria == 'S':
    cpu = random.randrange(1, 10)
    valor = int(input('Diga um valor: '))
    escolheu = str(input('Par ou Impar? [P/I] ')).upper().lstrip()[0]
    soma = valor+cpu
    print(f'Você jogou {valor} e o cpu jogou {cpu}. Total é {soma}')
    if escolheu != 'P' and escolheu != 'I':
        break
    if soma % 2 == 0 and escolheu == 'P':
        print('Você ganhou')
        cont +=1
    if soma % 2 != 0 and escolheu == 'P':
        print('Você perdeu')
        break
    if soma % 2 != 0 and escolheu == 'I':
        print('Você ganhou')
        cont += 1
    if soma % 2 == 0 and escolheu == 'I':
        print ('Você perdeu')
        break

print (f'{cont} vitorias vezes concecutivas.')