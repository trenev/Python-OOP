from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class RoomTest(TestCase):
    def setUp(self):
        self.room = Room("Trenevi", 2000, 4)

    def test_if_instance_set_success(self):
        self.assertEqual("Trenevi", self.room.family_name)
        self.assertEqual(4, self.room.members_count)
        self.assertEqual(2000, self.room.budget)
        self.assertListEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_property_when_greater_then_0_success(self):
        self.room.expenses = 100
        self.assertEqual(100, self.room.expenses)

    def test_expenses_property_when_less_then_0_expected_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = - 100
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses(self):
        child_1 = Child(5, 6, 7)
        child_2 = Child(7, 10)
        self.room.children = [child_1, child_2]
        self.room.calculate_expenses(self.room.children)
        self.assertEqual(1050, self.room.expenses)



if __name__ == "__main__":
    main()
