#CORES
# ANSI escape sequence        \033[codigo m
#                            style:texto:cor do fundo
#                             \033[0:33:44m

# Estilo 0 (nada), 1(negrito), 4(sublinhado), 7(inverter)
# Cor   30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(cinza)
# Fundo 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(ciano), 47(cinza)
# Então cor branco com fundo azul é: \033[0:33:44m

print('\033[0:30:41mTeste1')
print('\033[4:33:44mTeste2')
print('\033[1:35:43mTeste3')
print('\033[30:42mTeste4')
print('\033[mTeste5')
print('\033[7:30mTeste6')

print('')

print('\033[4:30:45m Olá, mundo! \033[m')
print('\033[0:30:47m Olá, mundo! \033[m')
print('\033[7:33:44m Olá, mundo! \033[m')

a = 'verde'
b = 'vermelho'
print ('O valores são \033[1:32m{}\033[m e \033[1:31m{}\033[m'.format(a,b))



"""
Cor	            Fonte	    Fundo
Preto	        \033[1;30m	\033[1;40m
Vermelho	    \033[1;31m	\033[1;41m
Verde	        \033[1;32m	\033[1;42m
Amarelo	        \033[1;33m	\033[1;43m
Azul	        \033[1;34m	\033[1;44m
Magenta	        \033[1;35m	\033[1;45m
Cyan	        \033[1;36m	\033[1;46m
Cinza Claro	    \033[1;37m	\033[1;47m
Cinza Escuro	\033[1;90m	\033[1;100m
Vermelho Claro	\033[1;91m	\033[1;101m
Verde Claro	    \033[1;92m	\033[1;102m
Amarelo Claro	\033[1;93m	\033[1;103m
Azul Claro	    \033[1;94m	\033[1;104m
Magenta Claro	\033[1;95m	\033[1;105m
Cyan Claro	    \033[1;96m	\033[1;106m
Branco	        \033[1;97m	\033[1;107m
Negrito	        \033[;1m	    -
Inverte	        \033[;7m	    -
Reset (remove formatação)	\033[0;0m

# Mais cores em: https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/

"""