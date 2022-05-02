from project.animals.animal import Animal, Bird
from project.food import Food


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        pass
        if self.__class__.__name__ not in Food.mapper_foods[food.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Animal.mapper_growth_weight[self.__class__.__name__]
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if self.__class__.__name__ not in Food.mapper_foods[food.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Animal.mapper_growth_weight[self.__class__.__name__]
        self.food_eaten += food.quantity
