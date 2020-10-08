''' TIPOS PRIMITIVOS
int   = 7, -4, 0, 875
float = 4.5, 0.0076, 7.0
bool  = True, False
str   = 'Olá' '7,5' ''
'''

'''
n1 = input ('Digite um número: ')
n2 = input ('Digite um número: ')
total = int(n1)+int(n2)
print('A soma é', total)
'''

#Outra solução
'''
numero1 = int(input ('Digite um número: '))
numero2 = int(input ('Digite um número: '))
total = numero1+numero2
print ('A soma vale {}'.format(total))
'''

#Identificando o tipo do que foi digitado
# n1 = int(input ('Digite um valor: '))
# print (type(n1))

'''
numero1 = int(input ('Digite um número: '))
numero2 = int(input ('Digite um número: '))
total = numero1+numero2
# print ('A soma entre {}'.format(numero1), 'e {}'.format(numero2), 'vale {}'.format(total))
# Simplificando o código
print ('A some entre {} e {} vale {}'.format(numero1, numero2, total))
'''

n = input('Digite algo: ')
print(n)
print(n.isnumeric())
print(n.isalnum())

