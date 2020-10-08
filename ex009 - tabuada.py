#entre com um número e retorne sua tabuada
n1 = int(input('Entre com um número: '))
n2 = 0
contador = 0
for tabuada in range(11):
    resultado = n1 * n2
    print ('A tabuada de {}x{}={}'.format(n1,n2,resultado))
    contador += 1
    n2 += 1