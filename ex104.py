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

def funcao(n):
    while True:
        lista=(0,1,2,3,4,5,6,7,8)
        if n not in lista:
            print('ERRO! Digite um número inteiro válido')
            n=int(input('Digite um número: '))
        else:
            print('saindo do laço')
            break


x = int(input('Digite um número: '))
funcao(x)
print(f'Você acabou de digitar o número {n}')

#print(f'Resultado é {resultado}')
