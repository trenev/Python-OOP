from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Caty", "Tiger", "roar")

    def test_is_instance_set(self):
        self.assertEqual("Caty", self.mammal.name)
        self.assertEqual("Tiger", self.mammal.type)
        self.assertEqual("roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected_result = "Caty makes roar"
        self.assertEqual(expected_result, result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(expected_result, result)

    def test_info(self):
        result = self.mammal.info()
        expected_result = "Caty is of type Tiger"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
