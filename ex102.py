#Função FATORIAL que recebe dois parametros
#Primeiro indica o número a calcular
#e o outro SHOW, que será um valor LOGICO (opcional)

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num:  O número a ser calculado
    :param show: (opcional) mostrar ou não o conta.
    :return:     O valor do Fatorial de um número
    """
    print(f'O fatorial de {num} com o show {show} é:')
    if show==True:
        f=1
        for c in range(num, 0, -1):
            f*=c
            print(c, end='')
            if c > 1:
                print(' x ', end='')
        print(f' = {f}')
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c

        print(f)


fatorial(5, True)
print()
help(fatorial)