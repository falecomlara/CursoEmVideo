#LEIA NOME E MEDIA DE UMA ALUNO
#GUARDANDO A SITUAÇÃO DO ALUNO (APROVADO/REPROVADO)

alunos = {}

alunos['nome'] = str(input('Nome: ')).title()
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
print()
print('<==== RESULTADO ====>')
print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
if (alunos["media"]) < 6:
    print('Situação é igual a Reprovado.')
else:
    print('Situação é igual a Aprovado.')
