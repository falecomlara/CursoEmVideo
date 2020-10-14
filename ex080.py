# digitar 6 valores numericos e uma lista
# ja na posicao correta, sem usar o sort
# no final mostra a lista ordenada na tela


numeros = []
maior = menor = 0
for c in range (0,6):
    num = int(input('Digite um valor: '))
    if c == 0:
        numeros.append(num)
        print('Adicionado na lista')
    elif num > numeros[-1]:
        numeros.append(num)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos<len(numeros):
            if num<=numeros[pos]:
                numeros.insert(pos, num)
                print('Adicionado na posição', pos)
                break
            pos+=1
print(f'Os valores digitados foram {numeros}')
