#digitar 7 valores em uma unica lista
# dentro desta lista, separados pares e impares
# no final mostre os pares e impares em ordem crescente

temporario = 0
numeros = [[],[]]  #criei uma lista composta

for c in range (1,8):
    temporario = int(input(f'Digite o {c} numero: ')) #esse é um valor temporário INTEIRO
    if temporario % 2 == 0:
        numeros[0].append(temporario) # se for PAR, joga na primeira lista
    else:
        numeros[1].append(temporario) # se for IMPAR, joga na segunda lista
print('-='*20)
numeros[0].sort() #Ordena apenas a primeira lista
print(f'Os números pares são..: {numeros[0]} ')

numeros[1].sort() #Ordena apenas a segunda lista
print(f'Os números impares são: {numeros[1]} ')