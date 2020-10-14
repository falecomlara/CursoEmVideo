# usuario digite uma expressão matematica qualquer
"""
digite uma expressao: ((a+b)*c)
expressao é valida

digite uma expressao: ((a+b)*c
expressao é invalida
"""
# usando uma lista para validar se é válido ou não

#Solução do Curso
expressao = str(input('Digite uma expressão: '))
pilha =[]
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha)>0:
            pilha.pop() #apaga o último dígito
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')


""" Minha resolução:
expressao = []
frase = str(input('Digite uma expressão matemática: '))
qtde = len(frase)
for c in range(qtde):
    expressao.insert(c, frase[c])
print(frase)
parenteses_e = expressao.count('(')
parenteses_d = expressao.count(')')
total = parenteses_e+parenteses_d
if total % 2 != 0:
    print('Expressão inválida')
else:
    print('Expressão correta')
"""