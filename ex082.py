# leia varios numeros e coloque em uma lista
# crie duas listas extras (pares e impares)
# ao final mostre as tres listas

#jogue em uma lista e no final, faz a analise, separando por listas
#completa, pares, impares

valores = []
par = []
impar = []
qtdep = qtdei = 0

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
        qtdep = par.count(num)
    else:
        impar.append(num)
        qtdei = impar.count(num)
    r = str(input('Quer continuar? [S/N] ')).rstrip()
    if r in 'Nn':
        break

print(f'A lista completa foi {valores}')
if qtdep>0:
    print(f'A lista de pares foi {par}')
if qtdei> 0:
    print(f'A lista impares foi  {impar}')