# Digite varios valores numéricos e cadastre uma lista
# caso o numero já existe, ele não irá cadastrar
# mostrar todos os numeros em ordem crescente

# Solução do curso:
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar...')

    r = str(input('Quer continuar [S/N] '))
    if r in 'Nn':
        break

numeros.sort()
print(f'Valores adicionados em ordem crescente foram: {numeros}')
print('=-='*30)


""" Minha resolução:
valores = []
continuar = 'S'
num = int(input('Digite um valor: '))
print('Valor adicionado com sucesso..')

while continuar == 'S':
    valores.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).upper().rstrip()
    if continuar == 'S':
        num = int(input('Digite um valor: '))
        for c in range(len(valores)):
            if valores[c-1] == num:
                print('Valor duplicado. Não vou adicionar...')
                valores.remove(num)
            print('Valor adicionado com sucesso..')

valores.sort()
print(f'Você digitou os valores {valores}')
"""
