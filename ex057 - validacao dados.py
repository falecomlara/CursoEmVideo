# ler sexo (somente M ou F
# se estiver errado, ler novamente

# RESPOSTA SIMPLES
sexo = str(input('Qual o seu sexo? [M/F] ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo inválido {}. '.format(sexo), end='')
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper()

print('Sexo {} registrado com sucesso'.format(sexo))
print('Fim exercício 057')


''' RESPOSTA AVANÇADA
sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0] # Tudo Maiusculo, Retira espaços e pega a posicao 0
while sexo != 'M' and sexo != 'F':
    print('Sexo inválido {}. '.format(sexo), end='')
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]

print('Sexo {} registrado com sucesso'.format(sexo.strip()[0]))
print('Fim exercício 057')
'''