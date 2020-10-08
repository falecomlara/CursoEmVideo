# quantos termos? e ao digitar 0 ele para

# refazer o numero 51, lendo o primeiro termo e a razao de uma PA
# mostrando os 10 termos
titulo = ' 10 TERMOS DE UMA PA com WHILE 2.0 '
x=len(titulo)
print('='*x)
print(titulo)
print('='*x)

primeiro = int(input('Primeiro termo '))
razao = int(input('Razão '))
termo = primeiro
cont = 1
zera = 1
final = 10

while cont <= 11:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
    if cont == 11:
        print ('PAUSA')
        pergunta = int(input('Quantos termos você quer mostrar mais? '))
        final = final + pergunta
        if pergunta == 0:
            break
        else:
            while zera < pergunta:
                print('{} -> '.format(termo), end='')
                termo += razao
                zera += 1
            cont -=1
            zera = 1

print ('-=-'*10)
print('Foram apresentados {} termos.'.format(final))