class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        filtered_pokemons = [element for element in self.pokemons if element.name == pokemon_name]
        if not filtered_pokemons:
            return "Pokemon is not caught"
        self.pokemons.remove(filtered_pokemons[0])
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for element in self.pokemons:
            result += f"- {element.pokemon_details()}\n"
        return result
