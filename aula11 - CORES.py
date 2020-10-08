#CORES
# ANSI escape sequence        \033[codigo m
#                            style:texto:cor do fundo
#                             \033[0:33:44m

# Estilo 0 (nada), 1(negrito), 4(sublinhado), 7(inverter)
# Cor   30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(cinza)
# Fundo 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(ciano), 47(cinza)
# Então cor branco com fundo azul é: \033[0:33:44m

print('\033[0:30:41mTeste')
print('\033[4:33:44mTeste')
print('\033[1:35:43mTeste')
print('\033[30:42mTeste')
print('\033[mTeste')
print('\033[7:30mTeste')

print('')

print('\033[4:30:45m Olá, mundo! \033[m')
print('\033[0:30:47m Olá, mundo! \033[m')
print('\033[7:33:44m Olá, mundo! \033[m')

a = 'verde'
b = 'vermelho'
print ('O valores são \033[1:32m{}\033[m e \033[1:31m{}\033[m'.format(a,b))