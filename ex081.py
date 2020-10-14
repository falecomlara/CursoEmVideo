# ler varios numeros e colocar em uma lista
# quantos digitados?
# a lista de valores ordenada em forma decrescente
# se o valor 5 foi digitado e se esta ou não na lista



numeros = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    print(f'Número {n} adicionado na lista.')

    r = str(input('Quer continuar? [S/N] ')).rstrip()
    if r in 'Nn':
        break

print('-=-'*20)
print(f'Você digitou {len(numeros)} elementos.')

numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')

if 5 in numeros:
    print('O número 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')