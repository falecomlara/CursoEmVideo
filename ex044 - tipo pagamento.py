'''
calcular o valor a ser pago
preco normal e condicao do pagamento

dinheiro ou cheque? 10% desconto
a vista no cartao? 5% desconto
2x no cartao = preco normal
3x ou mais no cartao = 20% juros
'''

mensagem = 'TIPO DE PAGAMENTO'
traco = len(mensagem)
print ('='*traco)
print(mensagem)
print ('='*traco)

preco = float(input('Preço das compras: R$'))
pgto  = int(input('''FORMA DE PAGAMENTO
 [1] Dinheiro / Cheque
 [2] à vista no cartão
 [3] 2x no cartão créd
 [4] 3x ou mais cartão
'''))
#vezes = 0

if pgto == 1:
    print('Sua compra de {} vai custar {} no final.'.format(preco, (preco-(preco*0.10))))
elif pgto == 2:
    print('Sua compra de {} vai custar {} no final.'.format(preco, (preco-(preco*0.05))))
elif pgto == 3:
    print('Sua compra de {}, será em duas parcelas de {} e vai custar {} no final.'.format(preco, (preco/2), preco))
elif pgto == 4:
    vezes = int(input('Quantas vezes?' ))
    if vezes == 1:
        print('Sua compra de {} vai custar {} no final.'.format(preco, (preco-(preco*0.10))))
    elif vezes == 2:
        print('Sua compra de {} vai custar {} no final.'.format(preco, (preco-(preco*0.05))))
    elif vezes > 2:
        print('Sua compra de {}, será dividido em {}, cada parcela será {} e vai custar {} no final.'.format
              (preco, vezes, round(((preco+(preco*0.20))/vezes),2), (preco+(preco*0.20))))
    else:
        print('Opção inválida')
else:
    print('Opção Inválida')


