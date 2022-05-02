from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    initial_members = 2
    cost_of_the_room = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, YoungCoupleWithChildren.initial_members + len(children))
        self.room_cost = YoungCoupleWithChildren.cost_of_the_room
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.children = list(children)
        for _ in range(len(children)):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())
        self.calculate_expenses(self.appliances, self.children)
