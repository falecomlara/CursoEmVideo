# jogador a criar megasena com palpites
# quantos jogos serao gerados?
# gerar 6 numeros (entre 1 e 60)
# não pode repetir

# No Curso usou FOR, na minha solução fiz WHILE

from random import randint
from time import sleep

lista = []
cont = jogos = feitos = 0

print('-='*20)
print('          JOGANDO NA MEGA SENA')
print('-='*20)

jogos = int(input('Quantos jogos você quer fazer? '))
print()
print('-='*3, f'SORTEANDO {jogos} JOGOS ', '-='*3)

while jogos != feitos:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont+=1
    if cont >=6:
        feitos+=1
        lista.sort()
        print(f'Jogo {feitos}: ', end='')
        sleep(1)
        print(lista)
        cont=0
        lista.clear()
print('-='*5, 'BOA SORTE', '-='*5)
