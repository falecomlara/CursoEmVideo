#Função Escreva, que recebe um texto qualquer como parametro e
#mostre uma mensagem com tamanho adaptável.


def escreva(msg):
    print(len(msg)*'=')
    print(msg.upper())
    print(len(msg)*'=')
    print()


#INICIO DO PROGRAMA
cont=0
while cont <5:
    cont+=1
    msg=str(input('Digite uma mensagem: '))
    escreva(msg)
