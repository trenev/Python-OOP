from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Pesho", 5, 100, 20)
        self.enemy = Hero("Gosho", 7, 150, 10)

    def test_is_instance_set(self):
        self.assertEqual("Pesho", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_str_representation(self):
        result = str(self.hero)
        expected_result = "Hero Pesho: 5 lvl\nHealth: 100\nDamage: 20\n"
        self.assertEqual(expected_result, result)

    def test_battle_with_itself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_hero_health_is_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_when_enemy_health_is_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ex.exception))

    def test_battle_when_hero_lose(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(20, self.hero.damage)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_battle_when_hero_win(self):
        self.enemy.health = 50
        result = self.hero.battle(self.enemy)
        self.assertEqual(35, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(10, self.enemy.damage)
        self.assertEqual("You win", result)

    def test_battle_when_result_is_draw(self):
        self.hero.health = 50
        self.enemy.health = 50
        result = self.hero.battle(self.enemy)
        self.assertEqual(-20, self.hero.health)
        self.assertEqual(20, self.hero.damage)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(10, self.enemy.damage)
        self.assertEqual("Draw", result)


if __name__ == "__main__":
    main()
