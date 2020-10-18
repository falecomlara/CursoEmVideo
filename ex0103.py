#Função FICHA que recebe dois parametros opcionais:
#o nomde de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador.

def ficha(nome=0, gols=0):
    if len(nome) == 0 and gols == 0:
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')
    elif len(nome) == 0 :
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome=str(input('Nome do jogador: '))
gols=int(input('Número de gols: ').isdigit())
ficha(nome, gols)

