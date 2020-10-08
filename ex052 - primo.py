#leia um número inteiro e diga se é primo
# divisil por 1 e por ele mesmo


num = int(input('Digite um número: '))

for c in range (1,num+1):
    print (c, end='')
    if  num % c == 0:
        print (' é primo')
    else:
        print (' não é primo')