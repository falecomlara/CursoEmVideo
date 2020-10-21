# comando leiadinheir()
# comando input e aceitar apenas valores monetários

import moeda
from CursoEmVideo.ex111.utilidadesCeV import dado

"""
def leiadinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip() # o número será tratado como string, para usarmos o 'isnumeric()'
        if n.isnumeric():   # aqui ele verifica se é uma string ou número
            valor=int(n)    # em caso verdadeiro (numérico), muda para inteiro e coloca em 'valor'
            ok = True       # coloca 'True' em 'ok'
        else:
            print(f'\033[0;31mERRO! "{n}" é um preço válido.\033[m')
        if ok:
            break
    return valor
"""

#Programa Principal
n = dado.leiadinheiro('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
moeda.resumo(n)

