#lista chamada numeros
#duas funcoes sorteia e somapar
#sorteia 5 numeros
#somapar vai mostrar a soma de todos os valores pares

from random import randrange

numero = []

def sorteia():
    for c in range(1,6):
        sorteado=randrange(1,10)
        numero.append(sorteado)
    print(numero)
    print(f'Quantidade sorteada {len(numero)}')
    somapares()


def somapares():
    pares=0
    for c,v in enumerate(numero):
        #print(f'chave {c} e valor {v}')
        if v % 2 == 0:
            pares+=v
    print(f'Numeros pares somados: {pares}')


sorteia()


# sobre o enumarate: http://devfuria.com.br/python/built-in-enumerate/