# criar sistema modularizado que permite cadastrar um nome e idade
# gravar em um arquivo simples: cadastrar e listar

from CursoEmVideo.interface import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #cabecalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        #cabecalho('Opção 2')
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).upper()
        if nome == '':
            nome = 'Desconhecido'
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema.. Até logo.')
        break
    else:
        print('ERRO! Digite uma opcao válida')
    sleep(0.5)