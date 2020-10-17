#FUNÇÃO CHAMADA AREA, que receba dimensoes de um terreno (largura x comprimento)
#e mostre a area do terreno

def calculararea(largura, comprimento):
    area=largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m.')


#INICIO DO PROGRAMA
print('CÁLCULO DE TERRENOS')
print('-'*19)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m):  '))


calculararea(largura, comprimento)