import pickle

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

def salvar_jogo(jogador):
    try:
        with open('database.db', 'wb')as arquivo:
            pickle.dump(jogador, arquivo)
            print('jogo salvo com sucesso')
    except Exception as error:
        print('erro ao salvar o jogo')
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb')as arquivo:
            jogador = pickle.load(arquivo)
            print('jogo carregado com sucesso')
            return jogador
    except Exception as error:
        print('erro ao carregar o jogo')

if __name__ == '__main__':
    print('----------------------------------')
    print('bem-vindo ao game pokemon RPG de terminal')
    print('----------------------------------')

    jogador = carregar_jogo()

    if not jogador:
        nome = input('ola, qual seu nome?: ')
        jogador = Player(nome)
        print('ola {}, esse é um mundo abitado por pokemons, apartir de agora sua missao é se tornar um mestre pokemon '.format(jogador))
        print('capture o maximo de pokemons que conseguir e lute contra os inimigos')
        jogador.mostrar_dinheiro()

        if jogador.pokemons:
            print('já vi que vc tem alguns pokemons')
            jogador.mostrar_pokemons()
        else:
            print('vc nn tem nenhum pokemon, portanto precisa escolher um')
            escolher_pokemon_inicial(jogador)

        print('pronto, agora que vc ja possui um pokemon, enfrente seu arqui-rival Gary ')
        gary = Inimigo(nome='Gary', pokemons=[PokemonPlanta('bubassauro', level=1)])
        jogador.batalhar(gary)
        salvar_jogo(jogador)

    while True:
        print('----------------------------------')
        print('o que deseja fazer?')
        print('1- exploxrar pelo mundo')
        print('2- lutar com um inimigo')
        print('3- mostrar pokedex')
        print('0- sair do jogo')
        escolha = input('sua escolha:')

        if escolha == '0':
            print('fechando o jogo')
            break
        elif escolha == '1':
            jogador.explorar()
            salvar_jogo(jogador)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            jogador.batalhar(inimigo_aleatorio)
            salvar_jogo(jogador)
        elif escolha == '3':
            jogador.mostrar_pokemons()
        else:
            print('escolha invalida')

    #escolher_pokemon_inicial(jogador)
    #jogador.capturar(PokemonSombrio('Umbreon', level=1))

    #inimigo1 =
    #jogador.batalhar(inimigo1)

    #jogador.explorar()

    #jogador.mostrar_pokemons()

#teste github desktop