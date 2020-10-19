# Módulo referente a AULA22

def fatorial(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f

def dobro(n):
    """
    --> Função para calcula o dobro de um número
    :param n: Entrada de um número inteiro
    :return:  Retornar o valor dobro
    """
    return n*2

def triplo(n):
    return  n*3