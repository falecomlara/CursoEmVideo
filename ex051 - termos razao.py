# leia o primeiro termo e a razao de uma PA
# no final, mostre os 10 primeiros termos dessa programação

titulo = ' 10 TERMOS DE UMA PA com FOR '
x=len(titulo)
print('='*x)
print(titulo)
print('='*x)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão:' ))
decimo = primeiro + (10-1) * razao

for c in range(primeiro, decimo + razao, razao):
    print ('{}'.format(c), end=' -> ')
print('ACABOU')