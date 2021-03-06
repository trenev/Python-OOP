class Cheetah:
    NEEDED_MONEY_TO_TEND = 60

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @staticmethod
    def get_needs():
        return Cheetah.NEEDED_MONEY_TO_TEND
