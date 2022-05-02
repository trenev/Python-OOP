from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 0.9

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + Car.INCREASED_FUEL_CONSUMPTION):
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.INCREASED_FUEL_CONSUMPTION)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 1.6

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + Truck.INCREASED_FUEL_CONSUMPTION):
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.INCREASED_FUEL_CONSUMPTION)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


# test car
import unittest


class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)


if __name__ == '__main__':
    unittest.main()
