# escreva um programa N inteiro e mostre os elementos da sequencia fibonacci
# usando while

titulo = ' SEQUÊNCIA FIBONACCI '
x=len(titulo)
print('='*x)
print(titulo)
print('='*x)

num = int(input('Quantos termos? '))
t1 = 0
t2 = 1
fib = 0
c = 3

print ('{} -> {} '.format(t1, t2), end='')
while c <= num:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print ('FIM')