#tabuada usando o laco (feito no exercicio 9)

titulo = 'GERADOR DE TABUADAS'
x=len(titulo)
print('='*x)
print(titulo)
print('='*x)

num = int(input('Digite um número: '))
for c in range(1,11):
    print('{} x {} = {}'.format(num,c,(num*c)))
