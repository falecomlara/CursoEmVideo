# digite uma frase e veja se ela é palindromo
# apos a soma, a sacada da casa, a torre da derrota, anotaram a data da maratona, o lobo ama o bolo

frase = ('a torre da derrota').strip().upper()
print(frase)

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('{} é um palindromo'.format(inverso))
else:
    print('{} Não é um palindromo'.format(junto))