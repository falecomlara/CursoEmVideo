# FUNÇÕES
def mostraLinha():
    print('-'*30)

def titulo(msg):
    mostraLinha()
    print(msg)
    mostraLinha()

titulo('SEJA BEM VINDO')
titulo('VOLTE SEMPRE')

titulo('CRIANDO FUNÇÃO DE SOMA')
#Criando uma função de SOMA
def somar(a,b):
    print(a+b)
    # ou posso colocar uma frase
    s = a + b
    print(f'A soma de {a}+{b} é = {s}')

somar(8,2)      #pedi para somar dois valores
somar(a=8, b=2) #eu também posso explicitar

titulo('EXEMPLO com Tuplas')
def contador(*num): # O * é que não importa a qtde de valores
    tamanho = len(num)
    print(f'Recebi os valores {num}, que tem ao todo {tamanho} números.')
    print()
    for c in num:
        print(f'Recebi os valores {num[c-1]}, ', end='')
    print()


contador(1,2,3)
print()

titulo('EXEMPLO com Listas')

def dobra(lista):
    pos=0
    while pos < len(lista):
        lista[pos]*=2
        pos+=1
    #print(lista)

valores=[0,2,5,0,4]

print(f'Imprimindo a lista: {valores}')
print('Agora usei a função "dobra(valores)" em cima dos valores')
dobra(valores)
print(f'Imprimindo os valores atualizados: {valores}')


titulo('EXEMPLO Desempacotando Valores')
def somando(* numeros): #essa função vai receber vários números
    s = 0
    for num in numeros:
        s+=num
    print(f'Somando os valores {numeros}, temos {s}')

somando(5,2)
somando(5,3,2,1)