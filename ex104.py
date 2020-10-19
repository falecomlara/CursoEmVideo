#Função LEIAINT que é semelhante ao input
#so que vai aceitar apenas valores numéricos

"""
def leiaint(n):
    globals(n)
    print('ERRO! Digite um número inteiro válido')

n=0
leiaint(1)
print(f'Você acabou de digitar o número {n}')
"""

def leiaInt(msg):
    """
    -> Esse é um parametro para validar se foi digitado um número inteiro
    :param msg: deve ser um número inteiro. valores em branco não será considerado numérico
    :return:    armazena o número e retorna no N
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg)) # o número será tratado como string, para usarmos o 'isnumeric()'
        if n.isnumeric():   # aqui ele verifica se é uma string ou número
            valor=int(n)    # em caso verdadeiro (numérico), muda para inteiro e coloca em 'valor'
            ok = True       # coloca 'True' em 'ok'
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

#print(f'Resultado é {resultado}')
