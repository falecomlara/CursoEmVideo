#Mini Sistema Interactive Help
#FIM ele encerra

def ajuda(n):
    help(n)
    while n not in "FIMfim":
        print('\033[0:30:47m')
        n = str(input('\033[30:42mDigite um comando: (FIM encerra) '))
        if n in "FIMfim":
            break
        else:
            help(n)
    print('FIM')



#INICIO DO PROGRAMA
comando = str(input('\033[30:42mDigite um comando: (FIM encerra) '))
ajuda(comando)