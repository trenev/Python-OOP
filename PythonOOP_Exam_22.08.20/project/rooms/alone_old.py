from project.rooms.room import Room


class AloneOld(Room):
    members = 1
    cost_of_the_room = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, AloneOld.members)
        self.room_cost = AloneOld.cost_of_the_room
