'''
escreva um numero inteiro e converta para (converter entre bases)
1 - binario
2 - octal
3 - hexadecimal
'''
mensagem = 'CONVERTER DE BASES'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

numero    = int(input('DIGITE UM NÚMERO: '))
converter = str(input('''[1] Binario 
[2] Octal
[3] Hexadecimal 
ESCOLHA: '''))

binario = bin(numero)
octal   = oct(numero)
hexa    = hex(numero)

if converter == '1':
    print('O número {} para Binário é {}'.format(numero,binario[2:]))
elif converter == '2':
    print('O número {} para Octal é {}'.format(numero,octal[2:]))
elif converter == '3':
    print('O número {} para Octal é {}'.format(numero, hexa[2:]))
else:
    print('Opção inválida ou não escolhida')