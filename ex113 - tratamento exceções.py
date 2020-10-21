# Reescreva o leiaint do ex104, incluindo a digitacao de um numero de tipo inválido
# crie uma funcao leiafloat() com a mesma funcionalidade

def leiaInt(msg=0):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário PAROU o programa')
            return 0
        else:
            return n


def leiaReal(msg=0):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário PAROU o programa')
            return 0
        else:
            return n



n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaReal('Digite um número real: ')
print(f'O valor inteiro digitado é {n1} e real foi {n2} ')
