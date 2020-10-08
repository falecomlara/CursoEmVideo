# leia a idade e o sexo
# cada pessoa deve perguntar (continuar)
# a quantos mais de 18
# quantos homens
# quantas mulhers < 20 anos

continuar = 'S'
idade18 = 0
sexom = 0
sexof = 0

while continuar == 'S':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().lstrip()[0]

    if idade > 18:
        idade18 += 1
    if sexo == 'M':
        sexom += 1
    if sexo == 'F' and idade < 20:
        sexof += 1

    continuar = str(input('Quer continuar? [S/N]')).upper().lstrip()[0]
    if continuar == 'S':
        continuar = 'S'
    if continuar == 'N':
        break

print('Fim')
print (f'Total de pessoas com mais de 18 anos: {idade18}')
print (f'Ao todo temos {sexom} homens cadastrados.')
print (f'E temos {sexof} mulher com menos de 20 anos')
