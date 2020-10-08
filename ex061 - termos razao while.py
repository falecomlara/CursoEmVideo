# refazer o numero 51, lendo o primeiro termo e a razao de uma PA
# mostrando os 10 termos
titulo = ' 10 TERMOS DE UMA PA com WHILE '
x=len(titulo)
print('='*x)
print(titulo)
print('='*x)

primeiro = int(input('Primeiro termo '))
razao = int(input('Razão '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print ('FIM')