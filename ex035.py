#ler tres retas e se pode ou não formar um triangulo
"""
Para construir um triângulo é necessário que a medida de qualquer um dos lados
seja menor que a soma das medidas dos outros dois
e maior que o valor absoluto da diferença entre essas medida.
"""

r1 = int(input('Digite um número: '))
r2 = int(input('Digite um número: '))
r3 = int(input('Digite um número: '))
somaa = r1+r2
somab = r2+r3
somac = r3+r1

subtraia = r1-r2
subtraib = r2-r3
subtraic = r3-r1

if r1 < somab and r1 > subtraib:
    print('Triangulo existe')
else:
    print('Triangulo não existe')