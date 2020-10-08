# mostrar todos os números pares entre 1 e 50

for c in range (1,51):
    resultado = c % 2
    if resultado == 0:
        print(c)