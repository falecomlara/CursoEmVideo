# leia varios inteiros no teclado, só vai parar quando digitar 999
# no final, mostre quantos foram digitados, desconsiderando o 999

n = cont = soma = 0

n = int(input('Digite um número: [999 para parar] '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: [999 para parar] '))

print ('Foram digitados {} numeros inteiros e a soma deles é {}.'.format(cont, soma))