# usuario digite uma expressão matematica qualquer
"""
digite uma expressao: ((a+b)*c)
expressao é valida

digite uma expressao: ((a+b)*c
expressao é invalida
"""
# usando uma lista para validar se é válido ou não

expressao = []
c=0

frase = str(input('Digite uma expressão matemática: '))
qtde = len(frase)
for c in range(qtde):
    expressao.insert(c, frase[c])
print(frase)
parenteses_e = expressao.count('(')
parenteses_d = expressao.count(')')
chaves_d = expressao.count('{')
chaves_e = expressao.count('}')
colchetes_d = expressao.count('[')
colchetes_e = expressao.count(']')
total = parenteses_e+parenteses_d+chaves_d+chaves_e+colchetes_d+colchetes_e
if total % 2 != 0:
    print('Expressão inválida')
else:
    print('Expressão correta')