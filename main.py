from pokemon import *

from pessoa import *

def escolher_pokemon_inicial(player):
    print("ola {}, escolha um pokemon para começar: ".format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    bubassaur = PokemonPlanta('Bubassauro', level=1)

    print('vc possui 3 opções:')
    print('1 -', pikachu)
    print('2 -', charmander)
    print('3 -', bubassaur)

    while True:
        escolha = input('escolha um pokemon:')

        if escolha == '1':
            player.capturar(pikachu)
            break

        elif escolha == '2':
            player.capturar(charmander)
            break

        elif escolha == '3':
            player.capturar(bubassaur)
            break

        else:
            print('opção inexistente, por favor escolha 1 2 ou 3 para escolher um pokemon')

jogador = Player(nome='Yumi')
escolher_pokemon_inicial(jogador)



