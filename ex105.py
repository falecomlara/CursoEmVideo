"""
funcao notas - receber varias notas
e retornar um dicionario com:
- quantidade notas adicionadas
- a maior nota
- a menor nota
- a media da turma
- a situacao
"""


def notas(*n, situacao=False):
    """
    ==> Cálculo de notas, dentro de uma função
    :param n:        Entrada de notas escolares do tipo Float
    :param situacao: Se 'True', retornará informações extras
    :return:         O return armazena o resultado e retorna para o programa
    """
    r = dict()
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=(sum(n)/len(n))
    if situacao:
        if r['media']>=6:
            r['situacao']='Aprovado'
        elif r['media']>=5:
            r['situacao']='Recuperação'
        else:
            r['situacao']='Reprovado'
    return r



#PROGRAMA PRINCIPAL
resp=notas(5,4,6,8.5, situacao=False)
print(resp)
resp=notas(5,4,6,8.5, situacao=True)
print(resp)

