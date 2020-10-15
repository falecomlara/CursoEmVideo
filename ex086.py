#matrix 3x3 e preencha os valores pelo teclado
# no final mostrar a matriz na tela, com a formatacao completa


matrix = [[],[],[]]

for c in range(0,3):
    for x in range (0,3):
        matrix[c].append(int(input(f'Digite um valor {c}x{x}> ')))


print('-='*20)
tamanho = (len(matrix))

for l in range(0,tamanho):
    for c in range(0,tamanho):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()