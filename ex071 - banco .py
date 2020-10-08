# simule um caixa eletronico
# valor a ser sacado? (INTEIRO)
# quantas cedulas de cada valor serao impressas

from math import floor

cinquenta = vinte = dez = um = 0
c50 = c20 = c10 = c1 = 0
resto = 0

num = int(input('Qual valor quer sacar? '))
if num >= 50:
    c50 = floor(num / 50)
    resto = num % 50
    num = resto

if num >= 20 and num <= 49 or resto >= 20 and resto <= 20:
    c20 = floor(num / 20)
    resto = num % 20
    num = resto

if num >= 10 and num <= 19 or resto >= 10 and resto <= 10:
    c10 = floor(num / 10)
    resto = num % 10
    num = resto

if num >= 1 and num <= 9 or resto >= 1 and resto <= 9:
    c1 = floor(num / 1)
    resto = num % 1
    num = resto

print('-=-'*10)
print(f'Total de {c50:.0f} cédulas de R$50')
print(f'Total de {c20:.0f} cédulas de R$20')
print(f'Total de {c10:.0f} cédulas de R$10')
print(f'Total de {c1:.0f} cédulas de R$1')
print('-=-'*10)