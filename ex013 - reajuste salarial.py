#mostre o salário e acrescente porcentagem

salario = float(input('Qual seu salário? '))
porcentagem = float(input ('Quanto % de aumento? '))
aumento = salario*(porcentagem/100)
final = salario + aumento

print('O salário no valor de {}, teve {}% de acréscimo e valerá {}.'.format(salario,porcentagem,final))
#print(produto, porcentagem, desconto, final)