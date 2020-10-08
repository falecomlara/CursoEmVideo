# leia dois valores e mostre um menu da tela
# 1 somar, multiplicar, qual maior?, trocar numeros, sair do programa

from time import sleep

trocar = True
sair = True

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

while sair != False:
    print("""
    |-------SISTEMA------|
    | [1] somar          |
    | [2] multiplicar    |
    | [3] qual maior?    |
    | [4] trocar números |
    | [5] sair programa  |
     \------------------/   
    """)
    opcao = int(input('Digite uma opção (1-5) '))
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    if opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    if opcao == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        if n1 < n2:
            print('{} é maior que {}.'.format(n2, n1))
        if n1 == n2:
            print('O {} tem o mesmo valor que {}.'.format(n1, n2))
    if opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    if opcao == 5:
        sair = False
    print('-=-' * 10)
    sleep(1)
print('Fim do programa. Volte sempre!')
