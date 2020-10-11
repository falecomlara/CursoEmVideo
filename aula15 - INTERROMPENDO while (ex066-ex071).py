# Instruções de break, fstrings

"""
cont = 1
while cont <= 10:
    print (cont, end='')
    cont +=1
    break #Quebra um loop
print(' acabou')
"""

n = s = 0
while True :
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(s)
print('A soma vale {}'.format(s))
print(f'A soma vale {s:-^10} (usando Fstring)') #Isso é uma FString