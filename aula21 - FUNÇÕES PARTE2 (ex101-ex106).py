
#Retorno de Variáveis

INTERACTIVE HELP - Ajuda de comandos do Python
help()                  Mostra ajuda de um comando
print(input.__doc__)    Um outro jeito de pedir ajudar



DOCSTRINGS - String de uma documentação
Para fazer uso da documentação, na sua função def, você adiciona " (3 vezes)
Veja um exemplo:

def calculararea(largura, comprimento):
    """
    -> Faz o cálculo
    :param largura: É a largura da sala
    :param comprimento: É o comprimento da sala
    :return: Ele irá calcular e retornar a área da sala
    Função criada por Eduardo Lara no curso de Python.
    """
    area=largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m.')

E ao executar help(calculararea) , será retornado as informações que foram digitadas.



PARAMETROS OPCIONAIS
Exemplo:
def somar(a,b,c):
    s=a+b+c
    print(f'A soma vale {s}.')

Eu tenho de chamar a def como somar(2,3,4). Mas o que acontece se digitar somar(2,3) ?
Iria retornar com erro. Então como resolver?

Eu tenho de mudar a def para um comando opcional:
def somar(a,b,c=0):

Ao fazer isso, estou definindo o C como parametro opcional. Ele pode existir, ou não. Porque
ele é OPCIONAL. E posso fazer isso com qualquer chamada na função. Exemplo:
def somar(a=0, b=0, c=0):

Ou eu posso informar qual valor tem de ser como padrão, caso o usuário não informe o valor.
Exemplo:  def somar(a=2, b=3, c=4):




ESCOPO DE VARIÁVEIS (local vs global):

def teste():
    x=8  <- variavel local (só funcional se chamar a função)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#PROGRAMA PRINCIPAL
n=2  <- variavel global. Pode chamar em qualquer momento
print(f'No programa principal, n vale {n}.')
teste()
print(f'No programa princial, não tem como saber o valor de X, porque é uma variavel local')

Agora se eu quiser que uma variável local, fique global, faço isso dentro da função:
def funcaolocal():
    global a
    a = 5

a=8
print(f'O retorno de A será 5 e não 8, porque o A foi explicito como global, dentro da função')
print(a)

Ao escrever global e definir a variável e seu valor, dentro da função,
ela passa a ser global.



RETORNO DE VALORES
É quanto eu utilizo o resultado de uma função, retornar para uma variável.
No exemplo, estarei fazendo uma soma e retornando para S:

def somar(a=0, b=0, c=0):
    s=a+b+c
    return s

resposta1 = somar(3,2,5)
resposta2 = somar(3,2)
resposta3 = somar(3)
print(f'Os resultados foram: {resposta1}, {resposta2}, {resposta3}')

E no meu programa, eu associo a função, para uma nova variável. Neste caso coloquei como
resposta1, resposta2 e resposta3.

Com as variáveis definidas, eu posso jogá-las em qualquer lugar. E no exemplo,
fiz um print personalizado.


EXEMPLOS:
def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f*=c
    return f

n=int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print()
f1=fatorial(5)
f2=fatorial(4)
f3=fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')


OUTRO EXEMPLO
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


print(par(2))
# Ele vai retornar como True