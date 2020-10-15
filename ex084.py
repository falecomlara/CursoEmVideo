# leia nome e peso e coloca numa lista
# quantos cadastrados?
# qual o maior peso e quem são?
# quem é o mais leve e quem são?


temporario = []  #ele é temporário porque irei pegar o dado, tratar e depois limpar
pessoas = []     # aqui ficará armazenado os dados cadastrados
maior = menor = 0

while True:
    temporario.append(str(input('Nome ')))  #lembre-se, é temporário essa lista
    temporario.append((float(input('Peso '))))

    if len(pessoas) == 0: # se eu não coloquei nada ainda, então...
        maior = menor = temporario[1] #pega o valor posicao 01 do temporário, que é o peso e joga em maior e menor
    else:
        if temporario[1] > maior:
            maior=temporario[1]
        if temporario[1] < menor:
            menor=temporario[1]

    pessoas.append(temporario[:]) #IMPORTANTE: gera lista composta. Ele pega o valor temporario e joga na nova lista
    temporario.clear() #Limpa os valores temporarios, para não duplicar, se precisar pedir novos dados

    resp = str(input('Quer continuar? S/N ')).rstrip()
    if resp in 'Nn':
        break

print(f'Os dados foram {pessoas}') #apenas para visualizar a lista composta

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.') #contagem de cadastrados criados que estao na lista

print(f'O maior peso foi de {maior}Kg, nas pessoas ', end='')
for p in pessoas: # vai ler toda a lista cadastrada
    if p[1]==maior: #na posicao 01 (que é o peso), compara se é maior
        print(f'[{p[0]}] ', end='') #em caso positivo, imprime o dado da posicao 0 (que é o nome)
print()
print(f'O menor peso foi de {menor}Kg, nas pessoas ', end='')
for p in pessoas:
    if p[1]==menor:
        print(f'[{p[0]}] ', end='')
print()

