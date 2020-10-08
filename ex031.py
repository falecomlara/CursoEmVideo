# distancia viagem em km
# calcule 0.50 por km para até 200km
# calcule 0.45 para mais de 200km

distancia = float(input('Qual a distância em KM? '))
if distancia <= 200:
    preco = 0.50 * distancia
    print ('Preço da passagem é {}'.format(preco))
else:
    preco = 0.45 * distancia
    print('Preco da passagem é {}'.format(preco))