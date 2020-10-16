"""
LER NOME E SEXO
- quantas pessoas cadastradas
- a media de idade do grupo
- uma lista com todas as mulheres
- uma lista com todas as pessoas com idade acima da media
"""
pessoas={}
galera=[]
soma=media=0

print('---= CADASTRO =---')
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome.: ')).title()
    while True:
        pessoas['sexo'] = str(input('Sexo.: ')).upper().lstrip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade']=int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            print('-=' * 15)
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp == 'N':
        break
print(pessoas)
print(galera)
print('-=' * 20)
print(f'Ao todo temos {len(galera)} cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'[ {p["nome"]} ]', end=' ')
print()
print(f'As pessoas que estão acima da média ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'[ {p["nome"]} ]', end=' ')
print()
print('-=' * 20)