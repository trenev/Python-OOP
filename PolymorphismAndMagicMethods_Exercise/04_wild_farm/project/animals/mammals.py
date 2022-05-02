from project.animals.animal import Animal, Mammal
from project.food import Food


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if self.__class__.__name__ not in Food.mapper_foods[food.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Animal.mapper_growth_weight[self.__class__.__name__]
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if self.__class__.__name__ not in Food.mapper_foods[food.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Animal.mapper_growth_weight[self.__class__.__name__]
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if self.__class__.__name__ not in Food.mapper_foods[food.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Animal.mapper_growth_weight[self.__class__.__name__]
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if self.__class__.__name__ not in Food.mapper_foods[food.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Animal.mapper_growth_weight[self.__class__.__name__]
        self.food_eaten += food.quantity
