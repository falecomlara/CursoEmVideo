"""
Uma tupla unica com nomes dos produtos e seus precos
no final mostre listagem de preços, organizando os dados em forma tabular
"""

listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90, 'Computador', 1200, 'Caneta', 2, 'Selos', 0.50,
            'Régua', 1.50, 'Estojo', 2, 'Geladeira', 2000, 'TV 50"', 2200, 'Mochila', 39.90, 'Compasso', 9.99)

linha = '-'
titulo = 'LISTAGEM DE PREÇOS'
qtde_titulo = len(titulo)
separador = '.'

print(linha * qtde_titulo * 2)
print(titulo.center(qtde_titulo * 2))
print(linha * qtde_titulo * 2)

item=0
preco=1
total=int(len(listagem)/2)

for c in range(total):
    x = listagem[item]
    y = listagem[preco]
    print((x.ljust(24, '.')), f'R$ {y:>8.2f}')

    item += 2
    preco += 2
print('-' * 36)

# FONTE:
# http://blog.evaldojunior.com.br/aulas/python/2008/11/23/curso-de-python-aula-5-matematica-recados-e-strings.html
# https://docs.python.org/pt-br/3/library/stdtypes.html
