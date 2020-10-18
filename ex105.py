"""
funcao notas - receber varias notas
e retornar um dicionario com:
- quantidade notas adicionadas
- a maior nota
- a menor nota
- a media da turma
- a situacao
"""

def nota(*n):
    aluno = {"notas":""}
    aluno["notas"]=n
    print(aluno)

    print(aluno, type(aluno))
    print(len(aluno))


#PROGRAMA PRINCIPAL
nota(5,4,6,2)
