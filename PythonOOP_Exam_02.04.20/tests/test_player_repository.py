from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class PlayerRepositoryTest(TestCase):
    def setUp(self):
        self.repository = PlayerRepository()

    def test_is_instance_set(self):
        self.assertEqual(0, self.repository.count)
        self.assertEqual([], self.repository.players)

    def test_add_when_card_not_exist(self):
        player = Beginner("Player")
        self.repository.add(player)
        self.assertEqual(1, self.repository.count)
        self.assertEqual([player], self.repository.players)

    def test_add_when_card_already_exist_expected_exception(self):
        player = Beginner("Player")
        self.repository.add(player)
        with self.assertRaises(ValueError) as ex:
            self.repository.add(Beginner("Player"))
        self.assertEqual("Player Player already exists!", str(ex.exception))
        self.assertEqual(1, self.repository.count)
        self.assertEqual([player], self.repository.players)

    def test_remove_when_name_is_valid(self):
        player = Beginner("Player")
        self.repository.add(player)
        self.repository.remove("Player")
        self.assertEqual(0, self.repository.count)
        self.assertEqual([], self.repository.players)

    def test_remove_when_name_is_empty_string_expected_exception(self):
        player = Beginner("Player")
        self.repository.add(player)
        with self.assertRaises(ValueError) as ex:
            self.repository.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))
        self.assertEqual(1, self.repository.count)
        self.assertEqual([player], self.repository.players)

    def test_find(self):
        player = Beginner("Player")
        self.repository.add(player)
        self.assertEqual(player, self.repository.find("Player"))


if __name__ == "__main__":
    main()
