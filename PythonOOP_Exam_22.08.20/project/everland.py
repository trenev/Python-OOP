from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        resut = 0
        for room in self.rooms:
            resut += room.expenses + room.room_cost
        return f"Monthly consumption: {resut:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses:
                result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have "
                              f"{room.budget - room.expenses:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        result = [f"Total population: {self.all_people_count}"]
        for room in self.rooms:
            result.append(str(room))
        return "\n".join(result)

    @property
    def all_people_count(self):
        return sum(room.members_count for room in self.rooms)
