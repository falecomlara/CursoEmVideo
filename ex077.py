# tupla com varias palavras
# mostrar cada palavra, quais são suas vogais

palavras = ('aprender', 'programas', 'python', 'linguagem', 'curso', 'grátis', 'estudar',
            'mercado', 'programador', 'futuro', 'aeiou', 'avião', 'não')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='' )
    for letra in p:
        if letra.lower() in 'aeiouãá':
            print(letra, end=' ')

""" Minha Solução
vogais = ''
qtde_palavras = (len(palavras))

for c in range(qtde_palavras):
    vogais = {x for x in (palavras[c]) if x not in 'qwrtypsdfghjklzxcvbnm'}
    print(f'Na palavra {palavras[c].upper()} temos as vogais {vogais}')
    vogais.clear()
"""