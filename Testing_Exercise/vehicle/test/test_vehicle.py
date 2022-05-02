from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 150)

    def test_is_instance_set(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_str_representation(self):
        result = str(self.vehicle)
        expected_result = "The vehicle has 150 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, result)

    def test_drive_when_fuel_is_enough(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_when_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_when_fuel_is_less_than_capacity(self):
        self.vehicle.drive(30)
        self.vehicle.refuel(10)
        self.assertEqual(22.5, self.vehicle.fuel)

    def test_refuel_when_fuel_is_above_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))


if __name__ == '__main__':
    main()
