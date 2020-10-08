# nome e preco de varios produtos
# continuar {s/n}
# qual total gasto
# quanto custa mais de 1000 reais
# nome do produto mais barato

soma = precobarato = mais1000 = preco = 0
continuar = 'S'
produtomaisbarato = ''

while continuar == 'S':
    produto = str(input('Produto: '))
    preco = float(input('Preço R$ '))

    soma += preco

    if preco > 1000:
        mais1000 += 1
    if precobarato == 0 or preco < precobarato:
        produtomaisbarato = produto
        precobarato = preco

    continuar = str(input('Continuar? [S/N] ')).upper().lstrip()[0]
    if continuar != 'S':
        break

print('-=-'*10)
print(f'O total da compra foi {soma:.2f}')
print(f'Temos {mais1000} produtos mais de R$ 1.000')
print(f'O produto mais barato foi {produtomaisbarato} que custou {precobarato:.2f}')