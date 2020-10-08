'''
Programa para emprestimo; Qual valor da casa? Salario? Quantos anos vai pagar?
calcule o valor da prestacao mensal, mas não pode exceder 30% do salario
'''
mensagem = 'SEJA BEM VINDO MINHA CASA MINHA VIDA'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

casa = float(input('Qual o valor da casa.? R$'))
sal  = float(input('Qual o seu salário...? R$'))
anos =   int(input('Quantos anos parcelar? '))
print ('='*traco)
pres = casa / (anos*12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, anos, pres))

if pres > ((sal*0.30)):
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')