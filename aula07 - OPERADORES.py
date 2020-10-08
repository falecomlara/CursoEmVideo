""" OPERADORES ARITMÉTICOS
+ adição, - subtração, * multiplicação, / divisão
** potencia, // divisao inteira, % resto da divisão
"""

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite um número: '))
n1 = int(9)
n2 = int(2)

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
inteira = n1 // n2
resto = n1 % n2
raiz = n1**(1/2)

print ('A adição de {} com {} é {}'.format(n1,n2,adicao))
print ('A subtracao de {} com {} é {}'.format(n1,n2,subtracao))
print ('A multiplicacao de {} com {} é {}'.format(n1,n2,multiplicacao))
print ('A potencia de {} com {} é {}'.format(n1,n2,potencia))
print ('A divisao real de {} com {} é {}'.format(n1,n2,divisao))
print ('A divisao inteira de {} com {} é {}'.format(n1,n2,inteira))
print ('O resto de {} dividido por {} é {}'.format(n1,n2,resto))
print ('A raiz quadrada de {} é {}'.format(n1,raiz))

#Comando extra
print('='*30)
print('O resultado é {:5}'.format(adicao),'!', end = ' >>> ') # O END no final do print é para juntar a linha
print('O resultado é {:>5}'.format(adicao),'!')

''' ORDEM DE PRECEDENCIA
1 ()
2 **
3 *, /, //, %
4 +, - 
'''