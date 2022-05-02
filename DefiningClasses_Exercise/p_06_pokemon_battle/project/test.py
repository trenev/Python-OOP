from p_06_pokemon_battle.project.pokemon import Pokemon
from p_06_pokemon_battle.project.trainer import Trainer

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())



import unittest


class PokemonTest(unittest.TestCase):
    def test_pokemon_init(self):
        pokemon = Pokemon("Pesho", 90)
        message = pokemon.pokemon_details()
        expected = "Pesho with health 90"
        self.assertEqual(message, expected)

    def test_trainer_init(self):
        trainer = Trainer("Stamat")
        message = f"{trainer.name} 0"
        expected = f"Stamat 0"
        self.assertEqual(message, expected)

    def test_adding_pokemon(self):
        trainer = Trainer("Stamat")
        pokemon = Pokemon("Pesho", 90)
        message = trainer.add_pokemon(pokemon)
        expected = "Caught Pesho with health 90"
        self.assertEqual(message, expected)

    def test_adding_already_addded_pokemon(self):
        trainer = Trainer("Stamat")
        pokemon = Pokemon("Pesho", 90)
        trainer.add_pokemon(pokemon)
        message = trainer.add_pokemon(pokemon)
        expected = "This pokemon is already caught"
        self.assertEqual(message, expected)

    def test_releasing_pokemon(self):
        trainer = Trainer("Stamat")
        pokemon = Pokemon("Pesho", 90)
        trainer.add_pokemon(pokemon)
        message = trainer.release_pokemon("Pesho")
        expected = "You have released Pesho"
        self.assertEqual(message, expected)

    def test_releasing_pokemon_that_is_not_caught(self):
        trainer = Trainer("Stamat")
        message = trainer.release_pokemon("Pesho")
        expected = "Pokemon is not caught"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()