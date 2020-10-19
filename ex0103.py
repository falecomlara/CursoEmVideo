#Função FICHA que recebe dois parametros opcionais:
#o nomde de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador.

def ficha(nome=0, gols=0):
    if gols.isnumeric():  # Lembra que no programa o gols é STRING? Agora você valida o dado aqui, dentro da função.
        gols = int(gols)
    else:
        gols = 0
    if len(nome) == 0 and gols == 0:
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')
    elif len(nome) == 0 :
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


#INICIO DO PROGRAMA
nome=str(input('Nome do jogador: '))
gols=str(input('Número de gols: ')) # Se você ler números, como STRINGS, você poderá validar no IF da função

ficha(nome, gols)

