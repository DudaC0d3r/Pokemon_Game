import random

from pokemon import *

NOMES = [
        'joao', 'isabela', 'lorena', 'francisco', 'ricardo',
        'patricia', 'marcelo', 'gustavo', 'geronimo'
]

POKEMONS = [
   PokemonFogo('charmander'),
   PokemonPlanta('bubasauro'),
   PokemonSombrio('zubat'),
   PokemonPsiquico('psyduck'),
   PokemonVeneno('eikans'),
   PokemonInseto('beedril'),
   PokemonSombrio('arboft'),
   PokemonEletrico('pikachu'),
   PokemonPsiquico('abra'),
   PokemonSombrio('mimikyu'),
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome

        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Pokemons de {}:'.format(self))
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
    tipo = 'inimigo'
    
    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

inimigo = Inimigo()
print(inimigo.tipo)
inimigo.mostrar_pokemons()


