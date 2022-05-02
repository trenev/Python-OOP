from unittest import TestCase, main

from project.card.magic_card import MagicCard


class MagicCardTest(TestCase):
    def setUp(self):
        self.card = MagicCard("Card")

    def test_is_instance_set(self):
        self.assertEqual("Card", self.card.name)
        self.assertEqual(5, self.card.damage_points)
        self.assertEqual(80, self.card.health_points)

    def test_name_property_when_empty_string_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.card.name = ""
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_damage_points_when_points_are_less_than_0_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.card.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_health_points_when_points_are_less_than_0_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.card.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    main()
