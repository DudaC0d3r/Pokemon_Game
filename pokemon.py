class Pokemon:
    def __init__(self, especie, level=1, nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return '{} ({})'.format(self.especie, self.level)

    def atacar(self, pokemon):
        print('{} atacou {}!'.format(self, pokemon))

class PokemonSolar(Pokemon):
    tipo = 'solar'

    def atacar(self, pokemon):
        print('{} lançou um ataque solar em {}'.format(self, pokemon))


class PokemonLunar(Pokemon):
    tipo = 'lunar'

    def atacar(self, pokemon):
        print('{} lançou um ataque lunar em {}'.format(self, pokemon))

meu_pokemon = PokemonSolar(level=1000000, especie='solgaleio')

pokemon_amigo = PokemonLunar('lunala', '10000')

meu_pokemon.atacar(pokemon_amigo)
pokemon_amigo.atacar(meu_pokemon)