from pokemon import *

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome

        else:
            self.nome = 'Anonimo'

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print('{} nao tem nenhum pokemon'.format(self))

class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))

class Inimigo(Pessoa):
    tipo = 'Inimigo'

meu_pokemon = PokemonSolar('Solgaleio', '100000')
meu_pokemon2 = PokemonLunar('Lunala', '100000')

eu = Player(nome='Yumi', pokemons=[meu_pokemon, meu_pokemon2])

print(eu)
eu.mostrar_pokemons()

pokemon_selvagem = PokemonLunar('Lunala')

eu.capturar(pokemon_selvagem)
