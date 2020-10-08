'''
refaca o desafio 35
que tipo do triangulo foi gerado?
todos iguais = equilatero
dois lados iguais = isosceles
todos os lados diferentes = escaleno
'''
mensagem = 'ANÁLISE DO TRIANGULO'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

r1 = int(input('Digite um número: '))
r2 = int(input('Digite um número: '))
r3 = int(input('Digite um número: '))
print('')
somaa = r1+r2
somab = r2+r3
somac = r3+r1

subtraia = r1-r2
subtraib = r2-r3
subtraic = r3-r1

if r1 < somab and r1 > subtraib:
    print ('TRINGULO EXISTE')
    if r1 == r2 == r3:
        print ('todos iguais = equilatero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print ('dois lados iguais = isosceles')
    else:
        print ('todos os lados diferentes = escaleno')
else:
    print('Triangulo NÃO existe')