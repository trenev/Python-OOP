from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    members = 1
    cost_of_the_room = 10

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, AloneYoung.members)
        self.room_cost = AloneYoung.cost_of_the_room
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
