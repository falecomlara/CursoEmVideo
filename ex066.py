# leia varios numeros inteiros
# so vai parar quando for 999
# no final mostre quantos foram digitados e qual a soma deles

soma = media = num = cont = 0

while num != 999:
    num = int(input('Digite um valor [999=parar] '))
    if num == 999:
        break
    soma += num
    cont += 1
media = soma/2
print (f'A soma dos {cont} valores é {soma} e a media é {media}')