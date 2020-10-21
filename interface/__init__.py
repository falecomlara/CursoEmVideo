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


def linha(tam = 42):
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('SISTEMA ARQUIVO v.1.0')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print((linha()))
    opc= leiaInt('Sua Opção: ')
    return opc


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # Read e Text (modo leitura)
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro abertura')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

            #print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # Append
    except:
        print('Houve um erro para abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao cadastrar')
        else:
            print(f'Novo registro {nome} adicionado.')
            a.close()