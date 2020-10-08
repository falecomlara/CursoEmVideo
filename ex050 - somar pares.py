# leia 6 numeros inteiros e mostre a soma apenas daqueles que sao pares
# impares é para desconsiderar

somar = 0
for c in range (1,7):
    num = int(input('Digite o {}° valor.: '.format(c)))
    if num % 2 == 0:
        somar = num + somar
print('A soma dos pares é: {}.'.format(somar))