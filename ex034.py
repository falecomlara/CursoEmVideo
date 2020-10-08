#salarios 1250 + 10%
#salarios 1000 + 15%
salario = float(input('Quanto você ganha? '))
if salario >= 1250:
    novosal = salario*0.10
else:
    novosal = salario*0.15
print('Seu salário {}'.format(salario), 'aumentou mais {}'.format(novosal), 'ficando em {}'.format(salario+novosal))