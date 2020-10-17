#funcao MAIOR que receba varios parametros
#analisa todos os parametros e qual é o maior


def maior(* numeros):
    print('Analisando os números...')
    nmaior = (sorted(numeros, reverse=True)[0])
    print(f'{numeros} Foram informados {len(nmaior)} valores ao todo.')
    print(f'O maior valor informado foi {sorted(nmaior, reverse=True)[0]}')


#INICIO DO PROGRAMA
numeros = []
cont=0
while cont<5:
    numeros.append(int(input('Digite um número: ')))
    cont+=1
print()
maior(numeros)
