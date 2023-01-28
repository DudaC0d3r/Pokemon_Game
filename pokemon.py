import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        self.level = level

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie


        self.ataque = self.level * 10
        self.vida = self.level * 20



    def __str__(self):
        return '{} ({})'.format(self.especie, self.level)

    def atacar(self, pokemon):
        print('{} tem {} pontos de vida'.format(self, self.vida))
        print('{} tem {} pontos de vida'.format(pokemon, pokemon.vida))

        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo




        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False

    def ataque_reduzido(self, pokemon):
        print('{} tem {} pontos de vida'.format(self, self.vida))
        print('{} tem {} pontos de vida'.format(pokemon, pokemon.vida))

        ataque_efetivo = int((self.ataque * random.random() * 0.5))
        pokemon.vida -= ataque_efetivo

        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False


class PokemonSolar(Pokemon):
    tipo = 'solar'

    def atacar(self, pokemon):
        print('{} lançou um ataque solar em {}'.format(self, pokemon))
        super().atacar(pokemon)

class PokemonLunar(Pokemon):
    tipo = 'lunar'

    def atacar(self, pokemon):
        print('{} lançou um ataque lunar em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print('{} lençou um ataque de fogo em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print('{} lançou um ataque eletrico em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonSombrio(Pokemon):
    tipo = 'sombrio'

    def atacar(self, pokemon):
        print('{} lençou um ataque sombrio em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, pokemon):
        print('{} lançou um ataque de agua em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFada(Pokemon):
    tipo = 'fada'

    def atacar(self, pokemon):
        print('{} lançou um ataque magico em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonPlanta(Pokemon):
    tipo = 'planta'

    def atacar(self, pokemon):
        print('{} lançou um ataque planta em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonPsiquico(Pokemon):
    tipo = 'psiquico'

    def atacar(self, pokemon):
        print('{} lançou um ataque psiquico em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonLutador(Pokemon):
    tipo = 'lutador'

    def atacar(self, pokemon):
        print('{} deu um golpe em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonVeneno(Pokemon):
    tipo = 'veneno'
    mana = 10

    def atacar(self, pokemon):
        print('{} lançou um ataque de veneno em {}'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonInseto(Pokemon):
    tipo = 'inseto'

    def atacar(self, pokemon):
        print('{} lançou um ataque de inseto em {}'.format(self, pokemon))
        return super().atacar(pokemon)



#meu_pokemon = PokemonSolar(level=1000000, especie='solgaleio')

#pokemon_amigo = PokemonLunar('lunala')



