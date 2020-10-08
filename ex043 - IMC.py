'''
peso e altura
calcular o IMC
18.5 < abaixo do peso
18.5 e 25 = peso ideal
25 a 30 = sobre peso
30 a 40 = obsesidade
40 acima = obesidade morbida
'''

mensagem = 'INDICE IMC'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

peso   = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

print ('Seu IMC é {}.'.format(round(imc,1)))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print ('Obesidade')
else:
    print ('Obesidade mórbida')