#TUPLAS - Variável Composto
# As tuplas são IMUTAVEIS
# (Tuplas) [Lista] {Dicionários}

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita', )

print ('Imprimindo a tupla...: ', lanche)
print ('Imprimindo posição 1.: ', lanche[1]) # na terceira posição
print ('Imprimindo posição 2.: ', lanche[2]) #me mostre do inicio, até o elemento 2 (mas ignora o elemento 2)
print ('Imprimindo posição -1: ', lanche[-1]) #de trás para frente
print ('Imprimindo:', lanche [1:3]) #vai do suco ate o final

# lanche[1] = 'Refrigerante' - Esse comando é errado porque tuplas são imutáveis
print('-=-'*10)


print (lanche[0:2])
print (lanche[1:]) #vai do suco ate o final
print (len(lanche))

print('-=-'*10)

for c in lanche:
    print(c)

print('-=-'*10)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-=-'*10)

for cont in range(0, len(lanche)):
    print (f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

print('-=-'*10)

for pos, comida in enumerate(lanche):
    print (f'Eu vou comer {comida} na posição {pos}')

print('-=-'*10)

print('Usando o sorted: ',sorted(lanche))

a = (2,6,4)
b = (5,8,1,3)
c = a+b

print(c)
print(sorted(c))
print(f'Tem {len(c)} elementos')
print(f'Contagem de números 4 é {c.count(4)} e na posição {c.index(4)}')

print('-=-'*10)

pessoa = ( 'Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa) # Você só pode apagar uma tupla inteira
print(pessoa)