#preco de um produto, e mostre novo preço com 5% de desconto

produto = float(input('Quanto custa? '))
porcentagem = float(input ('Quanto % de desconto? '))
desconto = produto*(porcentagem/100)
final = produto - desconto

print('O produto no valor de {}, tem {}% de desconto e custará {}.'.format(produto,porcentagem,final))
#print(produto, porcentagem, desconto, final)