#Manipulando Cadeia de Textos

'''
#FATIAMENTO (começo, fim, pulando)
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2]) # começa posição 9 e vai até posição 21, pulando de dois em dois
print(frase[:5])     # começa posição 0 e vai até a posição 5
print(frase[15:])    # começa posição 15 até o final
print(frase[9::3])   # começa posição 9 e vai até o final, pulando de três em três
'''

#ANALISE
'''
print(len(frase))       # quantos caracateres existe?
print(frase.count('o')) # quantas letras 'o' existe?
print(frase.count('o', 0,13)) # do Zero, até o Doze eu tenho Um 'o'
print(frase.find('deo')) # apresenta em que momento começou o 'deo', e o resultado é posição 11
print(frase.find('Android')) # se não existe, ele retorna como '-1'
print('curso' in frase)  # Sensitive case, se não encontrar, retorna como Falso
'''

#TRANSFORMACAO
'''
print(frase.replace('Python', 'Android')) # Susbtitui a palavra X com a palabra Y
print(frase.upper()) # deixa tudo em MAISCULO
print(frase.lower()) # deixa tudo em minúsculo
print(frase.capitalize()) # Inicia APENAS a primeiro caracatere como MAIÚSCULO
print(frase.title()) # Onde estiver espaço, ele transforma a primeira letra maiúscula
print(frase.rstrip()) # remove espaços da direita.
print(frase.lstrip()) # remove espaços da esquerda.
'''

#DIVISAO
'''
print(frase.split()) # onde houver espaço, ele causa uma divisão
'''

#JUNÇÃO
'''
print('-'.join(frase)) # adiciona um caracter em cada digito
'''

#EXTRAS - imprimir no formato
print("""
Sed egestas eget enim id condimentum. 
Nunc accumsan eu nisi vel fringilla. 
Vestibulum accumsan quis eros et malesuada. 
Donec accumsan nisl lacus, sit amet consequat dui vulputate vel. 
""")

 
