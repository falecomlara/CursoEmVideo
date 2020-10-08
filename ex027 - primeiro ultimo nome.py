# Digitar nome completo e separar o primeiro do último nome

nome = input('Qual o seu nome? ')
print('Muito prazer em te conhecer')
lista = (nome.split())
x = (len(lista))-1
print('Seu primeiro nome é: ', lista[0])
print('Seu último nome é: ', lista[x])