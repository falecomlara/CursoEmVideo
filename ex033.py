#ler tres numeros e qual é maior e menor
n1 = int(input('Digite um número A: '))
n2 = int(input('Digite um número B: '))
n3 = int(input('Digite um número C: '))
print('O maior é {}'.format(n1) if n1 > n2 and n1 > n3 else 'O maior é {}'.format(n2) if n2 > n1 and n2 > n3
else 'O maior é {}'.format(n3))
print('O menor é {}'.format(n1) if n1 < n2 and n1 < n3 else 'O menor é {}'.format(n2) if n2 < n1 and n2 < n3
else 'O menor é {}'.format(n3))