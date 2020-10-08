#gerar 5 numeros aleatorios e colocar numa tupla
#depois disso, mostrar a listagem dos numeros gerados
# qual o menor e maior

from random import randint

lista = []

for c in range(0,5):
    num = randint(1, 100)
    lista.append(num)
tupla = (tuple(lista))


print('Os valores sorteados são..: ', sorted(tupla))
print('O menor usando min() é....: ',min(tupla))
print('O maior usando max() é....: ',max(tupla))
print('')
print('A mesma solução, mas usando sorted()')
print('O menor com sorted()[0] é.: ',sorted(tupla)[0])
print('O maior com sorted()[-1] é: ', sorted(tupla)[-1])