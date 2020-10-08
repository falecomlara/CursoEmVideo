# mostra a tabuada para cada valor, quando o número for negativo

resultado = x = y = 0
n = 0

x = int(input('Quer ver qual tabuada? '))
while n < 11 :
    if x < 0:
        break
    if n == 10:
        n = x = y = 0
        x = int(input('Quer ver qual tabuada? '))
        if x < 0:
            break
    y += 1
    resultado = x*y
    print(f'{x} X {y} = {resultado} ')
    n += 1
print('Acabou')