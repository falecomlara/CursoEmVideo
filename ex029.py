# carro se ultrapassar 80 ele é multado
# cada km excedente pago 7 reais multa

velocidade = float(input('Qual sua velocidade? '))
multa = (velocidade-80)*7
print('Você foi multado em {} reais'.format(multa) if velocidade >80 else 'Tenha um bom dia e dirija com segurança')