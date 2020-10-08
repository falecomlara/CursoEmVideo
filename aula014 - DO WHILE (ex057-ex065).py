# REPETIDORES

'''
# FOR quando eu sei o limite
for c in range(1,10):
    print(c, end='')
print(' Fim for')

# While quando eu não sei o limite
c = 1
while c<10:
    print(c, end='')
    c=c+1
print(' Fim while')
'''

'''
for c in range(1,3):
    n = int(input('digite um valor'))
print ('Fim for')

n=1
r='S'
while r == 'S' :
    n=int(input('Digite um valor: '))
    r=str(input('Quer continuar? (s/n) ')).upper()
print('Fim while')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} impares.'. format(par,impar))