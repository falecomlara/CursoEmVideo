# soma de todos os numeros impares, que sao multiplos de 3, entre o intervalo 1 até 500

soma = 0
for c in range (1,501, 2):
    if c % 3 == 0:
        soma = soma+c
print ('A soma de todos os valores é {}'.format(soma))