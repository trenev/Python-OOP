from unittest import TestCase, main

from project.controller import Controller
from project.player.beginner import Beginner


class CardRepositoryTest(TestCase):
    def setUp(self):
        self.game = Controller()

    def test_add_player_when_player_is_beginner(self):
        self.assertEqual("Successfully added player of type Beginner with username: Player",
                         self.game.add_player("Beginner", "Player"))

    def test_add_player_when_player_is_advanced(self):
        self.assertEqual("Successfully added player of type Advanced with username: Player",
                         self.game.add_player("Advanced", "Player"))

    def test_add_card_when_card_is_magic_card(self):
        self.assertEqual("Successfully added card of type MagicCard with name: Card",
                         self.game.add_card("Magic", "Card"))

    def test_add_card_when_card_is_trap_card(self):
        self.assertEqual("Successfully added card of type TrapCard with name: Card",
                         self.game.add_card("Trap", "Card"))

    def test_add_player_card(self):
        self.game.add_player("Beginner", "Player")
        self.game.add_card("Trap", "Card")
        self.assertEqual("Successfully added card: Card to user: Player",
                         self.game.add_player_card("Player", "Card"))

    def test_fight(self):
        self.game.add_player("Beginner", "P1")
        self.game.add_player("Advanced", "P2")
        self.game.add_card("Trap", "C1")
        self.game.add_card("Magic", "C2")
        self.game.add_player_card("P1", "C1")
        self.game.add_player_card("P2", "C2")
        self.assertEqual("Attack user health 90 - Enemy user health 180", self.game.fight("P1", "P2"))

    def test_report(self):
        self.game.add_player("Beginner", "P1")
        self.game.add_player("Advanced", "P2")
        self.game.add_card("Trap", "C1")
        self.game.add_card("Magic", "C2")
        self.game.add_player_card("P1", "C1")
        self.game.add_player_card("P2", "C2")
        expected_result = "Username: P1 - Health: 50 - Cards 1\n" \
                          "### Card: C1 - Damage: 120\n" \
                          "Username: P2 - Health: 250 - Cards 1\n" \
                          "### Card: C2 - Damage: 5\n"
        self.assertEqual(expected_result, self.game.report())



if __name__ == "__main__":
    main()
