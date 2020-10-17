#função chamada contador que receba tres parametros
#inicio fim e passo
#1º de 1 ate 10 de 1 a 1
#2º de 10 ate 0, de 2 em 2
#3º personalizado pelo usuario

# def contador(inicio, fim, pulos):

from random import randrange
from time import sleep

def tracejados():
    print('-='*30)

def contagem(inicio, fim, pulos):
    print(f'Contagem de {inicio} até {fim} de {pulos} em {pulos}')
    for c in range(inicio, fim, pulos):
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')





contagem(10,0,-2)
tracejados()
contagem(1,11,1)
tracejados()

print('Agora é a sua vez de personalizar a contagem')
inicio=int(input('Início: '))
fim=int(input('Fim: '))
pulos=(int(input('Pulos: ')))
contagem(inicio, fim, pulos)

#fonte: https://pynative.com/python-range-function/