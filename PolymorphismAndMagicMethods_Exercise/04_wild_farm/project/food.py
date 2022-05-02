from abc import ABC, abstractmethod


class Food(ABC):
    mapper_foods = {"Vegetable": ["Hen", "Mouse", "Cat"],
                    "Fruit": ["Hen", "Mouse"],
                    "Meat": ["Hen", "Cat", "Dog", "Owl", "Tiger"],
                    "Seed": ["Hen"]}

    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)
