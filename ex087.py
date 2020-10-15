# aprimore o 086
# soma todos os valores pares digitados
# soma dos valores da terceira coluna
# o maior valor da segunda linha

matriz = [[], [], []]
par=terceira=maior=cont=0

for linha in range(0,3):
    for coluna in range (0, 3):
        matriz[linha].append(int(input(f'Digite um valor {linha}x{coluna}: ')))

        if (matriz[linha][coluna]) % 2 == 0:
            par += (matriz[linha][coluna])

    if (matriz[linha][2]) != 0:
        terceira += (matriz[linha][2])

for col in range(0,3): # Isso é SUPER IMPORTANTE para descobrir o MAIOR ou MENOR de um valor
    if col == 0:
        maior = (matriz[1][col])
    elif matriz[1][col]>maior:
        maior = (matriz[1][col])

print('-='*20)
tamanho = (len(matriz))

for l in range(0,tamanho):
    for c in range(0,tamanho):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')