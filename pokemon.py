import random

class Pokemon:
    def __init__(self, especie, level=random.randint(1, 100), nome=None):
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

class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print('{} lençou um ataque de fogo em {}'.format(self, pokemon))

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print('{} lançou um ataque de fogo em {}'.format(self, pokemon))

class PokemonSombrio(Pokemon):
    tipo = 'sombrio'

    def atacar(self, pokemon):
        print('{} lençou um ataque sombrio em {}'.format(self, pokemon))

class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, pokemon):
        print('{} lançou um ataque de agua em {}'.format(self, pokemon))

class PokemonFada(Pokemon):
    tipo = 'fada'

    def atacar(self, pokemon):
        print('{} lançou um ataque magico em {}'.format(self, pokemon))


class PokemonPlanta(Pokemon):
    tipo = 'planta'

    def atacar(self, pokemon):
        print('{} lançou um ataque planta em {}'.format(self, pokemon))


class PokemonPsiquico(Pokemon):
    tipo = 'psiquico'

    def atacar(self, pokemon):
        print('{} lançou um ataque psiquico em {}'.format(self, pokemon))


class PokemonLutador(Pokemon):
    tipo = 'lutador'

    def atacar(self, pokemon):
        print('{} deu um golpe em {}'.format(self, pokemon))


class PokemonVeneno(Pokemon):
    tipo = 'veneno'

    def atacar(self, pokemon):
        print('{} lançou um ataque de veneno em {}'.format(self, pokemon))


class PokemonInseto(Pokemon):
    tipo = 'inseto'

    def atacar(self, pokemon):
        print('{} lançou um ataque de inseto em {}'.format(self, pokemon))


meu_pokemon = PokemonSolar(level=1000000, especie='solgaleio')

pokemon_amigo = PokemonLunar('lunala')



