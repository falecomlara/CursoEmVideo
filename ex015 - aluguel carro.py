# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
dia = int(input('Quantos dias alugados? '))
km  = float(input('Quantos km rodei? '))
resultado = (dia*60)+(km*0.15)
print('Você alugou por {} e andou {} km. O total da conta é R${}.'.format(dia, km, resultado))