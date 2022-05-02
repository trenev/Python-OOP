from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.trap_card import TrapCard


class CardRepositoryTest(TestCase):
    def setUp(self):
        self.repository = CardRepository()

    def test_is_instance_set(self):
        self.assertEqual(0, self.repository.count)
        self.assertEqual([], self.repository.cards)

    def test_add_when_card_not_exist(self):
        card = TrapCard("Card")
        self.repository.add(card)
        self.assertEqual(1, self.repository.count)
        self.assertEqual([card], self.repository.cards)

    def test_add_when_card_already_exist_expected_exception(self):
        card = TrapCard("Card")
        self.repository.add(card)
        with self.assertRaises(ValueError) as ex:
            self.repository.add(TrapCard("Card"))
        self.assertEqual("Card Card already exists!", str(ex.exception))
        self.assertEqual(1, self.repository.count)
        self.assertEqual([card], self.repository.cards)

    def test_remove_when_name_is_valid(self):
        card = TrapCard("Card")
        self.repository.add(card)
        self.repository.remove("Card")
        self.assertEqual(0, self.repository.count)
        self.assertEqual([], self.repository.cards)

    def test_remove_when_name_is_empty_string_expected_exception(self):
        card = TrapCard("Card")
        self.repository.add(card)
        with self.assertRaises(ValueError) as ex:
            self.repository.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))
        self.assertEqual(1, self.repository.count)
        self.assertEqual([card], self.repository.cards)

    def test_find(self):
        card = TrapCard("Card")
        self.repository.add(card)
        self.assertEqual(card, self.repository.find("Card"))


if __name__ == "__main__":
    main()
