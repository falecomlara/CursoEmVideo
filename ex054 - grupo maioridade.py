# anos nascimento de 7 pessoas
# quantas pessoas sao maiores de 21 e quantos não sao mais de 21

from datetime import date
ano = date.today().year
print (ano)

idade =0
maior = 0
menor = 0
for c in range (1,4):
    nasceu = int(input('Que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano - nasceu
    if ano < nasceu:
        print('ANO INVÁLIDO')
    elif idade >= 21 and ano > nasceu:
        maior = maior +1
    elif idade < 21 :
        menor = menor +1
print('Menores de 21 são {} e Maiores de 21 são {}'.format(menor, maior))