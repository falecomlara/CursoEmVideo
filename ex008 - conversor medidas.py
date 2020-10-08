# leia valor em metros e converta em centimetros e milimitros
m = float(input('Quantos metros? '))
cm = m * 100
ml = m * 1000
print ('{}m é igual a {:.0f}cm e {:.0f}ml.'.format(m,cm,ml))