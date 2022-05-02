from unittest import TestCase, main

from project.player.beginner import Beginner


class BeginnerTest(TestCase):
    def setUp(self):
        self.advanced = Beginner("Player")

    def test_is_instance_set_success(self):
        self.assertEqual("Player", self.advanced.username)
        self.assertEqual(50, self.advanced.health)

    def test_is_dead_property_when_health_is_0(self):
        self.advanced.health = 0
        self.assertEqual(True, self.advanced.is_dead)

    def test_is_dead_property_when_health_is_greater_then_0(self):
        self.assertEqual(False, self.advanced.is_dead)

    def test_username_property_when_is_empty_string_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_health_property_when_is_less_than_0_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.health = -1
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_take_damage_when_damage_points_are_greater_than_0(self):
        self.advanced.take_damage(10)
        self.assertEqual(40, self.advanced.health)

    def test_take_damage_when_damage_points_are_less_than_0_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.take_damage(-10)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))
        self.assertEqual(50, self.advanced.health)


if __name__ == "__main__":
    main()
