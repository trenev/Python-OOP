from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class BattleFieldTest(TestCase):
    def test_fight(self):
        p1 = Beginner("P1")
        p2 = Advanced("P2")
        c1 = MagicCard("C1")
        c2 = TrapCard("C2")
        p1.card_repository.add(c1)
        p2.card_repository.add(c2)
        BattleField.fight(p1, p2)
        self.assertEqual(50, p1.health)
        self.assertEqual(220, p2.health)

    def test_fight_when_attacker_is_dead(self):
        p1 = Beginner("P1")
        p2 = Advanced("P2")
        c1 = MagicCard("C1")
        c2 = TrapCard("C2")
        p1.card_repository.add(c1)
        p2.card_repository.add(c2)
        p1.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(p1, p2)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_when_enemy_is_dead(self):
        p1 = Beginner("P1")
        p2 = Advanced("P2")
        c1 = MagicCard("C1")
        c2 = TrapCard("C2")
        p1.card_repository.add(c1)
        p2.card_repository.add(c2)
        p2.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(p1, p2)
        self.assertEqual("Player is dead!", str(ex.exception))


if __name__ == "__main__":
    main()
