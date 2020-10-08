'''
comparar dois numeros e da uma resposta:
x é maior, x é menor, os dois sao iguais
'''
mensagem = 'COMPARAR DOIS NÚMEROS'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número.: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num1 < num2:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')